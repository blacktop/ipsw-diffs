## routined

> `/usr/libexec/routined`

```diff

-990.0.10.0.0
-  __TEXT.__text: 0xc28
+1044.0.2.0.0
+  __TEXT.__text: 0xbd4
   __TEXT.__auth_stubs: 0x200
-  __TEXT.__objc_stubs: 0x2c0
-  __TEXT.__objc_methlist: 0xa4
-  __TEXT.__cstring: 0xec
-  __TEXT.__oslogstring: 0x158
-  __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__objc_classname: 0xe
-  __TEXT.__objc_methname: 0x300
-  __TEXT.__objc_methtype: 0x3a
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0x110
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x28
+  __TEXT.__objc_stubs: 0x300
+  __TEXT.__objc_methlist: 0x100
+  __TEXT.__cstring: 0xe6
+  __TEXT.__oslogstring: 0x50
+  __TEXT.__const: 0x8
+  __TEXT.__objc_classname: 0x24
+  __TEXT.__objc_methname: 0x3fa
+  __TEXT.__objc_methtype: 0x51
+  __TEXT.__unwind_info: 0x98
+  __DATA_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__const: 0x68
   __DATA_CONST.__cfstring: 0xa0
-  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x160
-  __DATA.__objc_selrefs: 0xe8
-  __DATA.__objc_ivar: 0x10
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0x30
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA.__objc_const: 0x290
+  __DATA.__objc_selrefs: 0x130
+  __DATA.__objc_ivar: 0x1c
+  __DATA.__objc_data: 0xa0
+  __DATA.__data: 0x18
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcoreroutine.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4E55A011-02EE-3108-80BB-F79A3BB8CF45
-  Functions: 23
-  Symbols:   49
-  CStrings:  63
+  UUID: EE7371C7-CC81-3C17-BF6D-0B388D68AB6A
+  Functions: 27
+  Symbols:   51
+  CStrings:  76
 
Symbols:
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSMutableArray
+ __NSConcreteGlobalBlock
+ _dispatch_once
+ _objc_msgSendSuper2
+ _objc_release_x1
+ _objc_release_x24
+ _objc_release_x28
+ _objc_retain_x19
+ _objc_retain_x23
- __Block_object_dispose
- __Unwind_Resume
- ___objc_personality_v0
- __os_log_impl
- _objc_release
- _objc_release_x23
- _objc_retain_x20
- _objc_retain_x22
CStrings:
+ "@\"RAAdpdVisitProvider\""
+ "RAAdpdVisitProvider"
+ "T@\"NSArray\",R,N,V_allDensityEvents"
+ "T@\"NSArray\",R,N,V_allProximityEvents"
+ "T@\"RAAdpdVisitProvider\",&,N,V_visitProvider"
+ "_allDensityEvents"
+ "_allProximityEvents"
+ "_visitProvider"
+ "addObject:"
+ "allDensityEvents"
+ "allProximityEvents"
+ "compare:"
+ "copy"
+ "defaultProvider"
+ "distantFuture"
+ "distantPast"
+ "endDate"
+ "setVisitProvider:"
+ "startDate"
+ "v8@?0"
+ "visitProvider"
- "An error was encountered while fetching density information, %@"
- "An error was encountered while fetching people counts, %@"
- "An error was encountered while fetching proximity events, %@"
- "ROUTINE APP"
- "There were no proximity events, so no query for people count events was executed"
- "count"
- "fetchPeopleCountEventsHistory:completionHandler:"
- "queryPeopleCount"

```
