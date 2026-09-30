## spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

-2314.2.0.0.0
-  __TEXT.__text: 0x7fad8
-  __TEXT.__auth_stubs: 0x1be0
-  __TEXT.__objc_stubs: 0x84c0
-  __TEXT.__objc_methlist: 0x4400
-  __TEXT.__const: 0x660
-  __TEXT.__cstring: 0x4d22
-  __TEXT.__oslogstring: 0x2ae3
-  __TEXT.__gcc_except_tab: 0x3cbc
-  __TEXT.__objc_classname: 0x710
-  __TEXT.__objc_methname: 0x99e5
-  __TEXT.__objc_methtype: 0xec9
+2314.4.1.0.1
+  __TEXT.__text: 0x80ca8
+  __TEXT.__auth_stubs: 0x1c20
+  __TEXT.__objc_stubs: 0x8560
+  __TEXT.__objc_methlist: 0x4480
+  __TEXT.__const: 0x6a8
+  __TEXT.__cstring: 0x4db8
+  __TEXT.__oslogstring: 0x2aef
+  __TEXT.__gcc_except_tab: 0x3cb8
+  __TEXT.__objc_classname: 0x712
+  __TEXT.__objc_methname: 0x9bae
+  __TEXT.__objc_methtype: 0xf06
   __TEXT.__dlopen_cstrs: 0x5e
   __TEXT.__unwind_info: 0x2160
-  __DATA_CONST.__auth_got: 0xe08
+  __DATA_CONST.__auth_got: 0xe28
   __DATA_CONST.__got: 0x5d0
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x3500
-  __DATA_CONST.__cfstring: 0x6be0
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__const: 0x3538
+  __DATA_CONST.__cfstring: 0x6c00
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __DATA_CONST.__objc_arraydata: 0x5c8
-  __DATA_CONST.__objc_arrayobj: 0x390
+  __DATA_CONST.__objc_arraydata: 0x5e0
+  __DATA_CONST.__objc_arrayobj: 0x3a8
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__objc_intobj: 0x318
-  __DATA.__objc_const: 0x7c80
-  __DATA.__objc_selrefs: 0x2750
-  __DATA.__objc_ivar: 0x4d4
+  __DATA_CONST.__objc_intobj: 0x330
+  __DATA.__objc_const: 0x7d40
+  __DATA.__objc_selrefs: 0x27c0
+  __DATA.__objc_ivar: 0x4e4
   __DATA.__objc_data: 0x2030
   __DATA.__data: 0x560
   __DATA.__bss: 0xae8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2479
-  Symbols:   631
-  CStrings:  3364
+  Functions: 2492
+  Symbols:   635
+  CStrings:  3407
 
Symbols:
+ _fputc
+ _fts_close
+ _fts_open
+ _fts_read
CStrings:
+ "setRepeatEventCount:"
+ "v32@0:8i16^v20I28"
+ "v20@0:8I16"
+ "### journal key %!@(MISSING) value: %!@(MISSING)"
+ "T^v,N,V_lastEventData"
+ "Log"
+ "setLastEventType:"
+ "paths"
+ "\n%!s(MISSING) pid: %!d(MISSING) time: %!s(MISSING)sbuild: %!s(MISSING)"
+ "setLastEventDataSize:"
+ "_lastEventDataSize"
+ "addEventWithTime:"
+ "Ti,N,V_lastEventType"
+ "^v16@0:8"
+ "ThrottlingChangedOn"
+ "I16@0:8"
+ "Repeat"
+ "_lastEventType"
+ "### removing SDB path %!@(MISSING)"
+ "lastEventDataSize"
+ "copyItemAtPath:toPath:error:"
+ "### error enumerating directory to files to purge: %!@(MISSING), %!@(MISSING)"
+ "### removing <%!@(MISSING)>"
+ "lastEventType"
+ "v16@?0r^{skg_playback_info=Ii(?={?=Id*}{?=dqq}{?=*}{?=**q}{?=d}{?=I})}8"
+ "ThrottlingChangedOff"
+ "### journalSizeUsed %!l(MISSING)ld %!l(MISSING)ld"
+ "addEventWithTime:data:dataSize:"
+ "initWithBytes:length:encoding:"
+ "skg_events_"
+ "!"
+ "\n%!s(MISSING) for item - bundle: %!s(MISSING) identifier: %!s(MISSING) oid: 0x%!l(MISSING)lx"
+ "TQ,N,V_lastEventDataSize"
+ "\n%!s(MISSING): %!s(MISSING)"
+ "\n%!s(MISSING) at time %!s(MISSING)"
+ "handleDiagnose"
+ "repeatEventCount"
+ "stringByDeletingPathExtension"
+ "lastEventData"
+ "^v"
+ "\nJournal was reset at time %!s(MISSING), size before reset: %!l(MISSING)lu, size after reset: %!l(MISSING)lu"
+ ", %!s(MISSING) %!d(MISSING) time(s)"
+ "diagnose"
+ "### mismatch repeat event %!d(MISSING) at offset %!l(MISSING)d\n"
+ "handleDiagnose:"
+ "### purging files of size %!l(MISSING)ld at <%!@(MISSING)>"
+ "TI,N,V_repeatEventCount"
+ "v24@0:8^v16"
+ "### Unable to purge file at path <%!@(MISSING)>"
+ "\n%!s(MISSING) - number %!d(MISSING)"
+ "setLastEventData:"
+ "_lastEventData"
+ "_repeatEventCount"
- "Test %!s(MISSING)\n"
- "Journal was reset at time %!s(MISSING), size before reset: %!l(MISSING)lu, size after reset: %!l(MISSING)lu\n"
- "%!s(MISSING) for item - bundle: %!s(MISSING) identifier: %!s(MISSING) oid: 0x%!l(MISSING)lx\n"
- "%!@(MISSING) error initializing store for indexType %!u(MISSING)"
- "DisableProcessingStateUpdater"
- "Test"
- "SKGUpdaterStore#instanceForIndexType Error %!d(MISSING) opening  %!s(MISSING)"
- "SKGUpdaterStore#instanceForIndexType Error %!@(MISSING) creating %!@(MISSING)"
- "v16@?0r^{skg_playback_info=I(?={?=Id*}{?=dqq}{?=*}{?=**q})}8"
- "CSJournalProcessor#_processOffsetAtOffset Error getting store for indexType %!u(MISSING)"
- "%!s(MISSING) pid: %!d(MISSING) time: %!s(MISSING)sbuild: %!s(MISSING)\n"

```
