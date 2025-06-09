## libMemoryResourceException.dylib

> `/usr/lib/libMemoryResourceException.dylib`

```diff

-281.100.5.0.0
-  __TEXT.__text: 0x18954
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_methlist: 0x1584
-  __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x1d40
-  __TEXT.__oslogstring: 0x90d
-  __TEXT.__gcc_except_tab: 0x3c0
+301.0.0.0.0
+  __TEXT.__text: 0x18cc4
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__objc_methlist: 0x154c
+  __TEXT.__const: 0x150
+  __TEXT.__cstring: 0x1dc4
+  __TEXT.__oslogstring: 0x9b5
+  __TEXT.__gcc_except_tab: 0x3cc
   __TEXT.__ustring: 0xd0
-  __TEXT.__unwind_info: 0x458
+  __TEXT.__unwind_info: 0x450
   __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x3877
-  __TEXT.__objc_methtype: 0x82f
-  __TEXT.__objc_stubs: 0x2bc0
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0xd90
+  __TEXT.__objc_methname: 0x382f
+  __TEXT.__objc_methtype: 0x81b
+  __TEXT.__objc_stubs: 0x2be0
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__const: 0xdf0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf18
+  __DATA_CONST.__objc_selrefs: 0xf20
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x668
+  __AUTH_CONST.__auth_got: 0x670
   __AUTH_CONST.__const: 0x250
-  __AUTH_CONST.__cfstring: 0x26c0
-  __AUTH_CONST.__objc_const: 0x2ef8
+  __AUTH_CONST.__cfstring: 0x2720
+  __AUTH_CONST.__objc_const: 0x2ea0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x25c
-  __DATA.__data: 0x440
+  __DATA.__objc_ivar: 0x258
+  __DATA.__data: 0x448
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_ivar: 0x1c
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x4178
+  __DATA_DIRTY.__bss: 0x4171
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement
   - /System/Library/PrivateFrameworks/Symbolication.framework/Symbolication
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C403C0C4-B258-3AB3-8A82-66E51D0FE106
-  Functions: 469
-  Symbols:   308
-  CStrings:  1630
+  UUID: 8DECBBE5-0A88-3A51-B876-B3BC3015EDE5
+  Functions: 468
+  Symbols:   310
+  CStrings:  1634
 
Symbols:
+ _IOAccelMemoryInfoErrorDomain
+ _MGGetStringAnswer
+ _memcmp
- _proc_pid_rusage
CStrings:
+ "Error adding nodes to VMUTaskMemoryScanner. Aborting memgraph generation. (%lu: MREMemgraphFailedReasonFailedCreateObjectGraph) Error: %@"
+ "Error generating VMUProcessObjectGraph. Aborting memgraph generation. (%lu: MREMemgraphFailedReasonFailedCreateObjectGraph)"
+ "Error generating VMUTaskMemoryScanner. Aborting memgraph generation. (%lu: MREMemgraphFailedReasonFailedCreateTaskMemoryScanner)"
+ "HWModelUniqueStr"
+ "MREExceptionConclaveFatalLimit"
+ "[5Q]"
+ "_drainDeferredReclaim"
+ "addSubrange:memoryTotal:"
+ "b!"
+ "code"
+ "domain"
+ "neural_nofootprint_total"
+ "neural_peak"
+ "v40@0:8{_NSRange=QQ}16^{?=QQQQQI}32"
+ "vm.reclaim.drain_pid"
- "@\"NSArray\"16@0:8"
- "Error adding nodes to VMUTaskMemoryScanner. Aborting memgraph generation. Error: %@"
- "Error generating VMUProcessObjectGraph. Aborting memgraph generation."
- "Error generating VMUTaskMemoryScanner. Aborting memgraph generation."
- "R!"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_memoryRegions"
- "[4Q]"
- "_gatherPhysFootprint"
- "_rangeList"
- "addSubrange:memoryTotal:pageSize:"
- "freeSubrangeList"
- "hw.model"
- "v48@0:8{_NSRange=QQ}16^{?=QQQQQI}32Q40"

```
