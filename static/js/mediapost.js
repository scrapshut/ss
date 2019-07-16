$('#people-entry').magicSuggest({
  data: [
    {name: 'Jimmy Hoffa'},
    {name: 'Elvis Presley'},
    {name: 'DB Cooper'},
    {name: 'Marylin Monroe'}
  ]
})

$('.post-form').on('click', '.open-overlay', function(e) {
  e.preventDefault()
  $($(this).data('target'))
    .removeClass('closed')
    .addClass('open')
  $('.post-form-backdrop')
    .removeClass('closed')
})
$('.post-form').on('click', '.post-form-overlay .close', function() {
  $(this).parents('.post-form-overlay')
    .addClass('closed')
    .removeClass('open')
  $('.post-form-backdrop')
    .addClass('closed')
})
