from datetime import datetime


def customize_card(project_name,author_name,filename):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    date,time=dt_string.split()
    string = '<div class="col-md-4"> <div class="card p-3 mb-2"> <div class="d-flex justify-content-between"> <div class="d-flex flex-row align-items-center"> <div class="icon"> <i class="bx bxl-mailchimp"></i> </div> <div class="ms-2 c-details"> <h6 class="mb-0">{author_name}</h6> <span>{date}</span> </div> </div> <div class="badge"> <span>{time}</span> </div> </div> <div class="mt-5"> <h3 class="heading">{project_name}</h3><br> <div class="badge"> <a href="$"><button class="btn btn-primary btn-sm"> <i class="fa fa-plus"></i> Download </button></a> </div> <div class="mt-5"></div> </div> </div> </div> \n <!-- <p>vetha</p> -->'.format(project_name=project_name,author_name=author_name,date=date,time=time)
    string=string.replace("$",'{{ url_for("download", filename="'+filename+'") }}')
    return string