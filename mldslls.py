#!/usr/bin/env python
if __name__ == "__main__":
    import logging

    log = logging.getLogger(__name__)
    logging.basicConfig(filename='C:\\Users\\RAZER\\Desktop\\mldslls_logs\\mldslls_log_1.log', encoding='utf-8',
                        filemode='w', level=logging.DEBUG)
    log.debug("Ran the server")
    import sys
    import os
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, root_dir)
    import mldslls
    mldslls.main()
