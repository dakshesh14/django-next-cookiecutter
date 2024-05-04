# Django and Next.js Monorepo with shadcn/ui monorepo

Start your new Django and Next.js Monorepo with shadcn/ui using this cookiecutter 🚀. Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter).

## Features

- Django and Next.js monorepo
- shadcn/ui
- Django 4.2.4 and Next.js 13.4.1
- Turbo repo
- and more...

## Requirements

- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js 14+](https://nodejs.org/en/download/)
- [pnpm](https://pnpm.io/installation)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)

## Setup

1. Generate a new Django and Next.js Monorepo project:

```bash
cookiecutter https://github.com/dakshesh14/django-next-cookiecutter.git
```

2. Change into the project directory:

```bash
cd <project_slug>
```

3. Install the dependencies:

```bash
pnpm install
pnpm prepare # for husky hooks
cd backend/{{ cookiecutter.project_slug }}_project && pip install -r requirements/local.txt # I recommend using a virtual environment
```

4. Start the development server:

```bash
turbo dev
cd backend/{{ cookiecutter.project_slug }}_project && python manage.py runserver
```

5. Open your browser and visit [http://localhost:3000](http://localhost:3000)

## License

This project is licensed under the terms of the [MIT License](/LICENSE).

## Commands

Here are some useful commands:

- `turbo ui:add <package>` - Add a package to the UI workspace.
- `turbo lint` - Lint the project.

## Contributing

Contributions are welcome! Please open an issue before making big changes. More information coming soon.

## Acknowledgements

Without the awesome community and tools, this project wouldn't be possible. Here are some of the tools and libraries used:

- [Django](https://www.djangoproject.com/)
- [Next.js](https://nextjs.org/)
- [shadcn/ui](https://ui.shadcn.com/)
- [Turbo](https://turbo.hotwired.dev/)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)

and many more...

## Future Plans

- [x] Add option to choose between /app or /pages router for Next.js
- [ ] Add documentation for backend and frontend on how to add more packages
- [ ] Add docker support

## Author

Made with ❤️ by [Dakshesh Jain](https://dakshesh.me)
