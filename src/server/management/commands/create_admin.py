from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError


class Command(createsuperuser.Command):
    help = 'Non-interactively create an admin user'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument('--password', default=None,
                            help='The password for the admin.')

    def handle(self, *args, **options):
        password = options.get('password')
        username = options.get('username')
        if password and not username:
            raise CommandError('--username is required if specifying --password')
            super(Command, self).handle(*args, **options)
        if password:
            database = options.get('database')
            db = self.UserModel._default_manager.db_manager(database)
            print('testing')
            try:
                user = db.get(username=username)
            except Exception as e:
                print('error, user does not exist', e)
                user = db.create(username=username)
                user.set_password(password)
                user.is_superuser = True
                user.is_staff = True
                user.is_active = True
                user.email = options.get('email')
            else:
                print('already existing user admin')
            user.save()
            print('user admin successfully registered')
