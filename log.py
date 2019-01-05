#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
log = logging.getLogger(__file__)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
if args.verbose >= 4:
  log.setLevel(logging.DEBUG)
elif args.verbose >= 3:
  log.setLevel(logging.INFO)
elif args.verbose >= 2:
  log.setLevel(logging.WARNING)
elif args.verbose >= 1:
  log.setLevel(logging.ERROR)
else:
  log.setLevel(logging.CRITICAL)
  
log.debug('debug')
log.info('info')
log.warning('warning')
log.error('error')
log.critical('critical')
