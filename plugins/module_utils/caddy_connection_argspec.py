# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Max Hösel <ansible@maxhoesel.de>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


caddyhost_argspec = dict(
    caddy_api=dict(type="str", default="http://localhost:2019"),
    timeout=dict(type="int", default=30)
)
