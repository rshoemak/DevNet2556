import os
from cli import cli,clip
  
cli('conf t; int Gig1; no service-policy output normal-egress-iwan8-shape')
cli('conf t; int Gig1; service-policy output linkdown-egress-iwan8-shape')
