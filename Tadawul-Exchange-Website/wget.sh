#!/bin/bash

pdf_url="$1"
pdf_name="pdfs/$2"
wget -O $pdf_name --user-agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0" $pdf_url