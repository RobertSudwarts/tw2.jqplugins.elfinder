<%namespace name="tw" module="tw2.core.mako_util"/>
<div ${tw.attrs(attrs=w.attrs)}></div>
<script type="text/javascript">
$(function() {
    $('#${w.selector}').${w.jqmethod}( ${w.options|n} );
});
</script>

