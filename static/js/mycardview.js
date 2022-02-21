//<script type="text/javascript">
  // var all_projects = JSON.parse('{{all_projects| safe }}');
  // when porting to server, need to implement AJAX and check status === 200
  // var position = document.getElementById('id_category');
  // var str_obj = JSON.stringify(passdata, undefined, 2); this is to get formatted string print out
  // passdata is an JSON object 
  // JSON objects first index to 1 obj, then use .key to get .value
  // Below construct a Javascript object to contains django ecoProject model
  var j_Project = {
    prj_id: 0,
    prj_name: "",
    priority: 0,
    category: 0,
    status: 0,
    description: "",
    stage: 0,
    create_date: "",
    start_date: "",
    end_date: "",
    close_date: "",
    site: 0,
    department: 0,
    prj_creator: "",
    updates: 0
  };
  function loadOneCard(json_unit) {
    var temp_field = json_unit.fields;
    var j_project = j_Project; 
    var card_html ="";
    j_project.prj_id = json_unit.pk;
    j_project.prj_name = temp_field.prj_name;
    j_project.priority = j_priority_choices[temp_field.priority];
    j_project.category = j_category_choices[temp_field.category];
    j_project.status = j_status_choices[temp_field.status];
    j_project.description = temp_field.description;
    j_project.stage = j_stage_choices[temp_field.current_stage];
    j_project.create_date = temp_field.create_date;
    j_project.start_date = temp_field.start_date;
    j_project.end_date = temp_field.end_date;
    j_project.close_date = temp_field.close_date;
    j_project.site = j_site_choices[temp_field.dpbg_site];
    j_project.department = j_department_choices[temp_field.pe_department];
    j_project.prj_creator = temp_field.prj_creator;
    j_project.updates = temp_field.updates;
    
    card_html = '<div id="pjm-single-card" class="col-md-4">';
    card_html += '<div class="h-100 p-3 bg-light border" style="border-radius: 10px;">';
    //card_html += '<div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">'; 
    card_html += '  <div class="prj-name headline-trim fw-bold fs-4 mb-3">';
    card_html += j_project.prj_name + '</div>';
    card_html += '  <div class="prj-desc">' + j_project.description + '</div> <hr>';
    card_html += '<ul style="padding-left:0; text: float;" type="none">';
    card_html += '<li>Priority:' + j_project.priority + '</li>';
    card_html += '<li>Status:' + j_project.status + '</li>';
    card_html += '<li>Category:' + j_project.category + '</li>';
    card_html += '<li>Stage:' + j_project.stage + '</li>';
    card_html += '<li>FX Site:' + j_project.site + '</li>';
    card_html += '<li>Department:' + j_project.department + '</li>';
    card_html += '<li>Start Date:' + j_project.start_date + '</li>';
    card_html += '<li>To finish by:' + j_project.end_date + '</li>';
    card_html += '<li>Close Date:' + j_project.close_date + '</li>';
    card_html += '<li class="prj-dri">DRI:' + j_project.prj_creator + '</li> </ul> <hr>';
    card_html += '<ul class="action-item" style="padding-left:1;">';
    card_html += '<li><a href="/tasks">See sub-tasks</a> </li>';
    card_html += '<li><a href="/modify">Modify project</a> </li>';
    card_html += '<li><a href="/addupdates">Add updates </a> </li> </ul>';
    card_html += '</div> </div>';
    return card_html;
  }
  function loadEmptyCard(row_length, num) {
    var card_html = "";
    var update_num = Number(num);
    console.log("Start of the loadEmpthCard: " + num);
    // output table header first
    card_html = '<div id="pjm-single-card" class="col-md-4">';
    card_html += '<div class="h-100 p-3 bg-light border" style="border-radius: 10px;">'; 
    card_html += '  <div class="prj-name headline-trim fw-semibold fs-5 mb-3"></div>';
    card_html += '  <div class="prj-desc"></div> <hr>';
    card_html += '<table class="prj-table">';
    for(var i=0; i<row_length; i++) {
        card_html += '<tr><td class="mytd-padding" style="width: 100px;"></td>';
        card_html += '<td class="mytd-padding"></td></tr>';
    };
    card_html += '</table><hr>';
    // output update items
    if(update_num > 0) {
      card_html += '<ul class="update-item" style="padding-left:0; text: float;" type="none">';
      for(i=0; i < update_num; i++) {
        card_html += '<li> added: </li>';
        card_html += '<li></li> <hr>';
      };
      card_html += '</ul>';
    };
    card_html += '<div class="action-item d-grid gap-2 d-sm-flex justify-content-sm-center mb-5">';
    //card_html += '<li><a href="/tasks">See sub-tasks</a> </li>';
    card_html += '<button id="btnEdit" style="width: 80px;" class="me-sm-3 btn btn-secondary" type="button">Modify</button>';
    card_html += '<button id="btnAdd" style="width: 156px;" class="px-4 me-sm-3 btn btn-secondary" type="button">Add Updates</button>';
    card_html += ' </div></div> </div>';
    return card_html;
  }

// </script>