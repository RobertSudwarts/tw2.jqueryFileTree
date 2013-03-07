<%namespace name="tw" module="tw2.core.mako_util"/>
<div ${tw.attrs(attrs=w.attrs)}> </div>

<script>
$(document).ready( function() {
var root_path = '/home/robertsudwarts/';
var scrpt = 'dir_fetch';
$('#my-widget').fileTree(${w.options | n}, 
      function(file) {
          console.log(file);
      });
  });
</script>