$(document).ready(function() {
    // ... (existing code)
  
    $('.article-link').on('click', function(event) {
      event.preventDefault(); // Prevent default link behavior
      const url = $(this).data('url');
      
      // Hide boxes 
      $('#sidebar, #topics-box, #most-viewed-box').hide();
      
      // Show article content area
      $('#article-content').show();
      
      // Fetch article content using AJAX
      $.get(url, function(response) {
        $('#article-content').html('<h2>' + response.article.title + '</h2><p>' + response.article.content + '</p>');
      });
    });
  });
  