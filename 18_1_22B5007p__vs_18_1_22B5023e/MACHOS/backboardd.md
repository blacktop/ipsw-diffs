## backboardd

> `/usr/libexec/backboardd`

```diff

-666.0.0.0.0
-  __TEXT.__text: 0x9e494
-  __TEXT.__auth_stubs: 0x1c40
-  __TEXT.__objc_stubs: 0xe960
-  __TEXT.__objc_methlist: 0x673c
+668.1.5.0.0
+  __TEXT.__text: 0x9f900
+  __TEXT.__auth_stubs: 0x1c50
+  __TEXT.__objc_stubs: 0xe9a0
+  __TEXT.__objc_methlist: 0x6774
   __TEXT.__const: 0x518
-  __TEXT.__gcc_except_tab: 0x4f70
-  __TEXT.__objc_methname: 0x148a9
-  __TEXT.__cstring: 0x6fdc
+  __TEXT.__gcc_except_tab: 0x4f54
+  __TEXT.__objc_methname: 0x14a54
+  __TEXT.__cstring: 0x711e
   __TEXT.__objc_classname: 0x1c70
-  __TEXT.__objc_methtype: 0x3ff8
-  __TEXT.__oslogstring: 0x9b4b
+  __TEXT.__objc_methtype: 0x3fed
+  __TEXT.__oslogstring: 0x9e5c
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x2968
-  __DATA_CONST.__auth_got: 0xe38
+  __TEXT.__unwind_info: 0x2980
+  __DATA_CONST.__auth_got: 0xe40
   __DATA_CONST.__got: 0xa18
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4a90
-  __DATA_CONST.__cfstring: 0x7c00
+  __DATA_CONST.__const: 0x4ad8
+  __DATA_CONST.__cfstring: 0x7ce0
   __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x240

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x13f78
-  __DATA.__objc_selrefs: 0x44c0
-  __DATA.__objc_ivar: 0xf00
+  __DATA.__objc_const: 0x14058
+  __DATA.__objc_selrefs: 0x44f8
+  __DATA.__objc_ivar: 0xf1c
   __DATA.__objc_data: 0x3930
   __DATA.__data: 0x1bb0
   __DATA.__bss: 0x418

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsp.dylib
-  Functions: 3110
-  Symbols:   783
-  CStrings:  6196
+  Functions: 3119
+  Symbols:   784
+  CStrings:  6239
 
Symbols:
+ _CFRunLoopWakeUp
CStrings:
+ "\x12\x13\x11"
+ "\x12\x1bA\x11#!\x1f\x04\""
+ " -> discrete scroll -- end phase (service disappeared)"
+ "%!@(MISSING) BKDisplayLink:%!p(MISSING) for %!@(MISSING)"
+ "%!@(MISSING): %!@(MISSING)"
+ "%!l(MISSING)lX"
+ "3\xf0A\xf0Q\xf1\xb1\xb1!B"
+ "B16@?0@\"CADisplay\"8"
+ "BKDisplayGetSystemIdentifiers"
+ "BKDisplayLink %!p(MISSING) _thread_invalidate"
+ "BKDisplayLink %!p(MISSING) _thread_invalidate already invalid"
+ "BKDisplayLink %!p(MISSING) invalidate finish"
+ "BKDisplayLink %!p(MISSING) invalidate start "
+ "BKDisplayLink init %!p(MISSING) %!{(MISSING)public}@"
+ "BKDisplayLink.m"
+ "BKDisplaySetSystemIdentifiers"
+ "Error unarchiving system identifiers"
+ "GetSystemIdentifiers failed to encode system identifiers"
+ "GetSystemIdentifiers: no active system identifiers"
+ "TDPS: cancelling button up %!X(MISSING)"
+ "_BKDisplayXXGetSystemIdentifiers"
+ "_BKDisplayXXSetSystemIdentifiers"
+ "_displayArrangement"
+ "_eventSequenceStartTimestamp"
+ "_haveDisplayAssociatedMouse"
+ "_haveUnassociatedMouse"
+ "_interestingDisplays"
+ "_locked_reevaluateDisplayLinkForReason:"
+ "_paused"
+ "_shouldHitTestForGestureBegan"
+ "_suppressButtonDown"
+ "_thread_displayLink"
+ "_thread_invalid"
+ "_thread_invalidate"
+ "_thread_setPaused:"
+ "activateForDataMigration"
+ "display %!{(MISSING)public}@ interesting because %!{(MISSING)public}@"
+ "display %!{(MISSING)public}@ uninteresting because %!{(MISSING)public}@"
+ "display arrangement changed"
+ "display became active -- %!@(MISSING)"
+ "display became inactive -- %!@(MISSING)"
+ "displays did change -- %!@(MISSING)"
+ "eventSequenceStartTimestamp"
+ "have display-specific device (sender:%!l(MISSING)lX display:%!{(MISSING)public}@)"
+ "have normal device (sender:%!l(MISSING)lX)"
+ "must -invalidate before dealloc"
+ "no region arrangement found; preserving previous:%!{(MISSING)public}@"
+ "no standard coalition pointer device"
+ "performSelector:onThread:withObject:waitUntilDone:"
+ "predicate changed"
+ "reevaluateActiveDisplaysWithReason:"
+ "reevaluateActiveDisplaysWithReason: %!{(MISSING)public}@"
+ "reevaluateDisplayArrangementForReason(%!{(MISSING)public}@)"
+ "reevaluateDisplayLink: no-op -- %!{(MISSING)public}@ -- paused:%!{(MISSING)BOOL}u"
+ "reevaluateDisplayLink: no-op -- no display link"
+ "services added"
+ "services removed"
+ "setSystemIdentifiers:"
+ "startServerWithDataMigration"
+ "startServerWithoutDataMigration"
+ "systemIdentifiers"
+ "we should not have a display link here. c:%!d(MISSING) d:%!d(MISSING) p:%!d(MISSING) u:%!d(MISSING)"
- "\x12\x19A\x11#!\x1f\x04\x12"
- "\x13\x12\x11"
- "#\xf0A\xf0Q\xf1\xb1\xb1!B"
- "%!@(MISSING) BKDisplayLink for %!@(MISSING)"
- "B20@0:8S16"
- "B24@?0@\"CADisplay\"8^@16"
- "_locked_reevaluateDisplayArrangementForReason -- %!{(MISSING)public}@"
- "device added"
- "device availability changed"
- "device removed"
- "display became active"
- "display became inactive"
- "displays did change"
- "hasGestureInPhase:"
- "performBlock:"
- "reevaluateActiveDisplays"
- "reevaluateDisplayLink: no-op %!{(MISSING)public}@"
- "scrollBeganTimestamp"
- "startSystemAppCheckInServer"

```
