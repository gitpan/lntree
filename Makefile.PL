# Makefile.PL -- Makefile for lntree
# $Id: Makefile.PL,v 1.1 1999-03-05 13:59:29+01 jv Exp $
# Author          : Johan Vromans
# Created On      : Mon Feb  8 11:46:56 1999
# Last Modified By: Johan Vromans
# Last Modified On: Fri Mar  5 13:59:27 1999
# Update Count    : 68
# Status          : Stable

# Verify perl version.
require 5.000;

use ExtUtils::MakeMaker;

my @scripts = map { "script/$_" } qw(lntree);

WriteMakefile
  (
   NAME         => 'lntree',
   AUTHOR	=> 'Johan Vromans (jvromans@squirrel.nl)',
   ABSTRACT	=> 'link identical files in source trees',
   VERSION_FROM => $scripts[0],
   PREREQ_PM	=> { 'Getopt::Long' => 2.00, 'IO' => 0 },
   EXE_FILES    => \@scripts,
   # *.pm files will be picked up automatically from ./lib
 );
