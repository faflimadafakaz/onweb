/*

This is a javascript file for omninotesweb
============

Author:  Suraj patil
Updated: January 2015
*/

$(document).ready(function(){

  /*on() is used instead of click because click can be used only on static elements, and on() is to be used when you add
  elements dynamically*/
  $('[data-toggle="tooltip"]').tooltip();
  
  if ($('#message').html()==''){ $('.notification').addClass('hidden')} 
  $('.notification-close').click(function(){$('.notification').fadeOut('slow')})

	$('#category_form').addClass('hidden');

    /*$('.floating-action-icon').popover({
	  animation: true,
	  
	  });*/
  $(document).on("click", '.floating-action-icon', addNote);
  
  $(document).on("click", ".edit-note", editNote);
  
  $('[data-toggle="popover"]').popover({}); //for category's more actions

   //$(document).on("click", '.note-close',closeDelete); //when you delete a note, the x on the top right corner

   $(document).on('click','.open-note', openNote); //when you want to open a note in full screen, the second icon on the bottom right corner from the right

   $(document).on('click','.hashtag', hashTag); //function to handle search by hashtag *TODO*

   
   $('#add_category').click(function(){
       $('#category_form').toggleClass('hidden');
   });

});

function closeDelete(){
  var note = $(this).parent().parent().parent();
  note.fadeOut('slow');
  note.remove();

}

function addNote(){
  var addNoteModal = $('#addNoteModal');
  addNoteModal.modal('show');
}

function editNote(){
  var addNoteModal = $('#addNoteModal');
  var form = addNoteModal.find('form')
  
  var element = $(this);
  var cont=element.parent().parent().siblings().contents().toArray();
  var note_body =cont[2].data;
  var note_title = cont[0].data;
  var cont = element.siblings().contents().toArray()
  var category = cont[0].data;
  var created = cont[1].data;
  var permalink = cont[2].data;
  console.log(permalink);
  form.prop('action','/edit_note/'+permalink);
  category = category.trim();
    
  var children = $('#id_category').children();
  
  var cat_id =0;
  $.each(children, function(index, value){
     if(value.innerHTML==category){
        cat_id=index;
     }
  });

  
  $('select>option:eq('+cat_id+')').prop('selected', true);
  
  addNoteModal.find('.modal-title').text('Edit note');
  $('#id_title').val(note_title);
  $('#id_content').val(note_body);
  addNoteModal.content = note_body;
  addNoteModal.modal('show');
  
}

function openNote(){
  var element = $(this);
  var cont=element.parent().parent().siblings().contents().toArray();
  var note_body =cont[2].data;
  var note_title = cont[0].data;
  var cont = element.siblings().contents().toArray()
  var category = cont[0].data;
  var created = cont[1].data;


  var ONmodal = $('#openNoteModal');
  ONmodal.find('.modal-title').text(note_title);
  ONmodal.find('.modal-body').text(note_body);
  ONmodal.find('.category').text(category);
  ONmodal.find('.created').text(created);
  ONmodal.modal('show');
}

function hashTag(){
  alert($(this).html());
}
