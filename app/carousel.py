carousel = """\
<div class="accordion" id="accordionExample">

<div class="collapse show" id="collapseOne" data-parent="#accordionExample">
  <div class="card card-body">
    <p>Seite 1</p>
  </div>
</div>

<div class="collapse" id="collapseTwo" data-parent="#accordionExample">
  <div class="card card-body">
    <p>Seite 2</p>
  </div>
</div>

<div class="collapse" id="collapseTree" data-parent="#accordionExample">
  <div class="card card-body">
    <p>Seite 3</p>
  </div>
</div>


<nav aria-label="Page navigation example">
  <ul class="pagination justify-content-center">
    <li class="page-item"><a class="page-link" data-toggle="collapse" href="#collapseOne">1</a></li>
    <li class="page-item"><a class="page-link" data-toggle="collapse" href="#/services/impressum">2</a></li>
    <li class="page-item"><a class="page-link" data-toggle="collapse" href="#collapseTree">3</a></li>
  </ul>
</nav>
</div>
"""
