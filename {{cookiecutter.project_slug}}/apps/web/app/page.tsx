export default function Page() {
  return (
    <div
    className="h-screen flex items-center justify-center bg-gray-100"
    >
      <h1
      className="text-4xl font-bold text-gray-800"
      >
        {{cookiecutter.project_name}}
      </h1>
      <p>
        {{cookiecutter.project_description}}
      </p>
    </div>
  );
}
