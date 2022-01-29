<template>
  <div class="Row">
    <td>{{ user.first_name }}</td>
    <td>{{ user.last_name }}</td>
  </div>
</template>

<script>
export default {
  name: 'Row',
  props: {
    user: {
      type: Object
    },
  },
};
</script>