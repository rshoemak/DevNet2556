import os
from cli import cli,clip
  
cli('conf t; int Gig1; no service-policy output linkdown-egress-shape')
cli('conf t; int Gig1; service-policy output normal-egress-shape')
