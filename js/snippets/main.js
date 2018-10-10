// Code cell snippets

define([
    'jquery',
    'base/js/namespace',
    'base/js/dialog',
    'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.9-1/crypto-js.js'
], function(
    $,
    Jupyter,
    dialog
) {
    "use strict";

/* TODO
  1. Fill in cell with code
  2. Push Button to hash current cell
  3. Hash current cell
  4. Add hash to meta data of current cell under "hash" key
  5. Create a new cell next
  6. Add hash to meta data of next cell under "previous_hash" key

*/
      // function to place snippet modal manager
      function hash_cell() {

        var prev_cell = Jupyter.notebook.select_prev();
        var next_cell = Jupyter.notebook.select_next();


        var selected_cell = Jupyter.notebook.get_selected_cell();
        var selected_content = selected_cell.get_text();


        var hash = CryptoJS.SHA256(selected_content);
        var result = CryptoJS.enc.Hex.stringify(hash);


        prev_cell.metadata['hash']

        /*
        var modal_content = $('<p/>').html("Please provide a name for this snippet.");
        modal_content.append($('<br><br>'));
        modal_content.append($('<input type="text" name="snippet-name"/>'));

        Jupyter.keyboard_manager.register_events(modal_content);

        dialog.modal({
          title: 'Add Code Cell to Snippet Manager',
          body: modal_content,
          buttons: {
            Cancel: {
              'class': 'btn-danger'
            },
            OK: {
              'class': 'btn-primary',
              'click': function() {
                var snippet_name = $('input[name=snippet-name]').val();
                var snippet_tags = this.metadata.tags
                add_snippet_to_storage(snippet_name, selected_content, snippet_tags);
              }
            }
          }
        });
        */
      }


      function load_ipython_extension() {
        if (!Jupyter.toolbar) {
          $([Jupyter.events]).on("app_initialized.NotebookApp", place_snippet_manager_buttons);
          return;
        }

        if ($(".snippet-manager-buttons").length === 0) {
          Jupyter.toolbar.add_buttons_group([{
              'label': 'Hash',
              'icon': 'fa-database',
              'callback': hash_cell,
              'id': 'hash-cell',
              'class': 'snippet-manager-buttons'
            }
          ]);
        }
      }



    // will be called when the nbextension is loaded
    function load_extension() {
        Jupyter.notebook.config.loaded.then(initialize); // trigger loading config parameters

        //$.getJSON("https://single-cell-codesnippets.firebaseio.com/.json", function(data) {
        //$.getJSON(Jupyter.notebook.base_url+"nbextensions/snippets/snippets.json", function(data) {
        $.getJSON(Jupyter.notebook.base_url+"nbextensions/snippets/snippets.json", function(data) {
            // Add the header as the top option, does nothing on click
            var option = $("<option></option>")
                         .attr("id", "snippet_header")
                         .text("Snippets");
            $("select#snippet_picker").append(option);

            // Add options for each code snippet in the snippets.json file
            $.each(data['snippets'], function(key, snippet) {
                var option = $("<option></option>")
                             .attr("value", snippet['name'])
                             .text(snippet['name'])
                             .attr("code", snippet['code']);//.join('\n'));
                $("select#snippet_picker").append(option);
            });
        })
        .error(function(jqXHR, textStatus, errorThrown) {
            // Add an error message if the JSON fails to load
            var option = $("<option></option>")
                         .attr("value", 'ERROR')
                         .text('Error: failed to load snippets!')
                         .attr("code", "");
            $("select#snippet_picker").append(option);
        });

    };

    var insert_cell = function() {
        var selected_snippet = $("select#snippet_picker").find(":selected");

        if (selected_snippet.attr("name") != 'header') {
            var code = selected_snippet.attr("code");
            var new_cell = Jupyter.notebook.insert_cell_above('code');
            new_cell.set_text(code);
            new_cell.focus_cell();

            $("option#snippet_header").prop("selected",true);
        }
    };

    // return public methods
    return {
        load_ipython_extension : load_extension
    };
});
