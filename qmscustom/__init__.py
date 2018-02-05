# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QMSCustom
                                 A QGIS plugin
 QMS Custom para arbolado
                             -------------------
        begin                : 2018-02-05
        copyright            : (C) 2018 by CIGA
        email                : cesar.benjamin@enesmorelia.unam.mx
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QMSCustom class from file QMSCustom.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qms_custom import QMSCustom
    return QMSCustom(iface)
