## ansf.t603x.release.im4p

> `Firmware/ansf.t603x.release.im4p`

```diff

   __TEXT.text_first: 0x44c0
-  __TEXT.__text: 0x19abd0
-  __TEXT.shared: 0xc710
-  __TEXT.read: 0x6060
+  __TEXT.__text: 0x19ae04
+  __TEXT.shared: 0xcec8
+  __TEXT.read: 0x6114
   __TEXT._rtk_mtab: 0x540
-  __TEXT.__const: 0xa828
-  __TEXT.__cstring: 0x200a2
+  __TEXT.__const: 0xa818
+  __TEXT.__cstring: 0x2037d
   __TEXT.idle_hooks: 0x10
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

   __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x412818
+  __DATA.__zerofill: 0x4128b8
   Functions: 0
   Symbols:   0
-  CStrings:  3554
+  CStrings:  3574
 
Sections:
~ __TEXT._rtk_mtab : content changed
~ __TEXT.idle_hooks : content changed
~ __DATA.__data : content changed
~ __DATA.__const : content changed
~ __DATA.core_globals : content changed
CStrings:
+ " Sanitize_Run -> %ums"
+ "!Sanitize_IsActive()"
+ "587"
+ "587~383"
+ "Abort Pad: Flow %u , Band: %u"
+ "AppleStorageFirmwarePreASP3-587~383"
+ "BG_TODO_SET(BG.todo.sanitize) was called when host is idle"
+ "Could not find blocker"
+ "Invalid Sanitize phase %d"
+ "Sanitize already in progress, phase=%d"
+ "Sanitize started"
+ "Sanitize: Phase 1 complete abort pad"
+ "Sanitize: Phase 2 complete, abort pad done"
+ "Sanitize: Phase 3 complete, marked %u bands with Must"
+ "Sanitize: Phase 4 complete, GC done"
+ "Sanitize: Phase 5 complete, marked %u bands with Must and Special"
+ "Sanitize: Phase 6 complete, GC done"
+ "mark band %u"
+ "mark band %u, isOpen %u"
+ "sanitize cmd drop - configuration not supported"
+ "sanitize cmd drop - during another sanitize phase %u"
+ "sanitize cmd drop - invalid system state: DM %u Clog %u shn %u"
+ "sanitize cmd: sanact %u, cfg 0x%x, op 0x%x"
+ "sanitize.c"
- "582"
- "582~5020"
- "AppleStorageFirmwarePreASP3-582~5020"
- "Unexpected tag: %d, segIdx: %d"

```
