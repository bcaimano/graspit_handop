//######################################################################
//
// GraspIt!
// Copyright (C) 2002-2009  Columbia University in the City of New York.
// All rights reserved.
//
// This software is protected under a Research and Educational Use
// Only license, (found in the file LICENSE.txt), that you should have
// received with this distribution.
//
// Author(s):  Andrew T. Miller 
//
// $Id: gwsProjDlg.h,v 1.4 2009/03/25 22:10:14 cmatei Exp $
//
//######################################################################

/*! \file
  \brief Defines the GWSProjDlg, the Grasp wrench space projection dialog box.
*/
#ifndef GWSPROJDLG_H
#define GWSPROJDLG_H

#include <QDialog>
#include <set>
#include "ui_gwsProjDlgBase.h"

class QButtonGroup;

//! Creates and controls the grasp wrench space projection dialog box.
/*!
  Using this interface the user can create a 3-dimensional projection of the
  6D grasp wrench space (GWS).  The dialog has 6 check boxes, one for 
  each of the 3 force and 3 torque
  coordinates.  For each coordinate there is also a box to enter the fixed
  projection value.  Once the user has chosen 3 coordinates to fix they may
  create a projection of the GWS by clicking OK.
*/
class GWSProjDlg : public QDialog, public Ui::GWSProjDlgBase
{ 
    Q_OBJECT

public:
    GWSProjDlg( QWidget * parent = 0 );
    ~GWSProjDlg();

    //! Holds the set of indexes of the coordinates that are currently fixed.
    std::set<int> whichFixed;

public slots:
    virtual void coordBoxClicked( int buttonNum );

protected:
    //! A pointer to the group of 6 check boxes
    QButtonGroup *coordButtonGroup;
};

#endif // GWSPROJDLG_H
