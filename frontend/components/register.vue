<template>
    <div class="flex min-h-full flex-1 flex-col justify-center py-12 sm:px-6 lg:px-8">
            <div class="sm:mx-auto sm:w-full sm:max-w-md">
              <img class="mx-auto h-10 w-auto" src="/favicon.ico" alt="Your Company" />
              <h2 class="mt-8 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Register for your account!</h2>
            </div>

            <div class=" sm:mx-auto sm:w-full sm:max-w-[480px]">
              <div class="bg-white px-6 py-12 shadow sm:rounded-lg sm:px-12">
                <form class="space-y-6" action="#" method="POST">
                  <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Username</label>
                      <div class="mt-2">
                        <input id="email" name="email" type="email" autocomplete="email" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                      </div>
                  <div>
                    <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
                    <div class="mt-2">
                      <input id="email" name="email" type="email" autocomplete="email" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                    </div>
                  </div>

                  <div>
                    <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
                
                    <div class="mt-2">
                      <input id="password" name="password" type="password" autocomplete="current-password" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                    </div>
                  </div>
                  <div>
                      <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Confirm Password</label>
                
                      <div class="mt-2">
                        <input id="password" name="password" type="password" autocomplete="current-password" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                      </div>
                    </div>
                  <div>
                    <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Register</button>
                  </div>
                  <div>
                    Already have an account? 
                    <a href="/signin" class="text-indigo-600 hover:text-indigo-500">
                        Sign in here!
                    </a>
                  </div>
                </form>
              </div>

         
            </div>
          </div>


</template>

<script>

export default {
    name: 'Register'
}
</script>
