<template>
  <div class="container-fluid">
    <header>
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">
          <b-icon icon="person-check-fill"></b-icon>&nbsp;GitTesters
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <router-link to="/" class="nav-link">Home</router-link>
            </li>
          </ul>
        </div>
      </nav>
    </header>

    <main role="main">
      <slot name="content"></slot>
    </main>

    <footer class="text-muted">
      <div class="container">
        <p>Este exemplo de álbum é &copy; Bootstrap, mas, por favor, baixe e customize por conta própria.</p>
      </div>
    </footer>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>