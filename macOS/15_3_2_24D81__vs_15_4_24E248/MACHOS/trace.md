## trace

> `/usr/bin/trace`

```diff

-629.80.2.0.0
-  __TEXT.__text: 0xdef8
-  __TEXT.__auth_stubs: 0xc50
-  __TEXT.__const: 0x84c
-  __TEXT.__cstring: 0x1e61
+649.100.6.0.0
+  __TEXT.__text: 0xdb00
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__const: 0x85c
+  __TEXT.__cstring: 0x1ed1
   __TEXT.__swift5_typeref: 0x32c
   __TEXT.__swift5_capture: 0x60
   __TEXT.__constg_swiftt: 0x1f8

   __TEXT.__swift5_assocty: 0x110
   __TEXT.__objc_methname: 0x29
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x360
+  __TEXT.__unwind_info: 0x328
   __TEXT.__eh_frame: 0x2b4
-  __DATA_CONST.__auth_got: 0x628
+  __DATA_CONST.__auth_got: 0x620
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x2a0
   __DATA_CONST.__const: 0x8d8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 9B922951-4F3D-3C04-B5AA-CB5AE336D611
-  Functions: 296
-  Symbols:   342
-  CStrings:  204
+  UUID: 81CD7D7F-D225-3B06-85EB-798360FA2BD8
+  Functions: 292
+  Symbols:   341
+  CStrings:  203
 
Symbols:
+ _swift_deallocPartialClassInstance
- _strcmp
- _swift_bridgeObjectRetain_n
CStrings:
+ "\n\ntrace record: record a trace file\n    $ trace record myworkload\n        [... Ctrl-C to stop ...]\n    $ trace record myworkload --Logging:enable-logs --end-after-duration 5s\n    $ trace record myworkload --plan profile --omit Symbolication\n    $ trace record myworkload --end-on-notification stop-myworkload-trace\n        [... elsewhere `notifyutil -p stop-myworkload-trace` ...]\n    $ trace record /tmp/trace-path.atrc --compress\n\ntrace amend: add data to a file\n    $ trace amend myworkload-003.atrc --add Symbolication\n\ntrace trim: trim a file based on kdebug event times\n    $ trace trim myworkload-002.atrc --from +1s --to +2s\n\ntrace providers: print information about Logging, Symbolication, etc.\n\ntrace plans: print detailed information about tracing approaches\n\nSee `man trace` for more information."
- "\n\ntrace record: record a trace file\n    $ trace record myworkload\n        [... Ctrl-C to stop ...]\n    $ trace record myworkload --Logging:enable-logs --end-after-duration 5s\n    $ trace record myworkload --plan profile --omit Symbolication\n    $ trace record myworkload --end-on-notification stop-myworkload-trace\n        [... elsewhere `notifyutil -p stop-myworkload-trace` ...]\n    $ trace record /tmp/trace-path.atrc --compress\ntrace amend: add data to a file:\n    $ trace amend myworkload-003.atrc --add Symbolication\ntrace providers: print information about Logging, Symbolication, etc.\ntrace plans: print detailed information about tracing approaches\n\nSee `man trace` for more information."
- "-X"

```
