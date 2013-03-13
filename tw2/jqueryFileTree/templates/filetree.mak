<%namespace name="tw" module="tw2.core.mako_util"/>
<div ${tw.attrs(attrs=w.attrs)}> </div>
<script>
$(document).ready( function() {
$('#${w.id}').fileTree(${w.options | n}, 
      function(file) {
          console.log(file);
      });
  });
</script>
