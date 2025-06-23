## RoseControllerLib

> `/System/Library/Extensions/AppleSPURose.kext/PlugIns/RoseControllerLib.plugin/RoseControllerLib`

```diff

-1046.0.1.0.0
-  __TEXT.__text: 0x8270
-  __TEXT.__auth_stubs: 0x530
+1046.0.3.0.0
+  __TEXT.__text: 0x8120
+  __TEXT.__auth_stubs: 0x540
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0xc72
   __TEXT.__gcc_except_tab: 0x1e4
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x368
-  __DATA_CONST.__auth_got: 0x2a0
+  __TEXT.__unwind_info: 0x370
+  __DATA_CONST.__auth_got: 0x2a8
   __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x190
+  __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__cfstring: 0xc0
   __DATA.__data: 0x220
   __DATA.__common: 0x8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: AE1046CF-C635-37C7-B318-4F9D2E4DFF7F
-  Functions: 287
-  Symbols:   203
+  UUID: 92E3A50E-02F5-3501-865D-08282980657C
+  Functions: 288
+  Symbols:   205
   CStrings:  119
 
Symbols:
+ __NSConcreteGlobalBlock
+ _dispatch_barrier_sync
Functions:
~ __ZN14RoseController4StopEv : 84 -> 104
+ sub_2354
~ __ZN14RoseController5ResetEv : 328 -> 252
~ __ZN14RoseController19_flushResponseQueueEv : 116 -> 124
~ __ZN14RoseController17ResetSMCRoseStateEv : 320 -> 244
~ __ZN14RoseController20RegisterEventHandlerEPFvPvS0_mES0_ : 192 -> 108
~ __ZN14RoseController15ServiceCallbackEjPv : 1000 -> 856
~ __ZN14RoseController28_dispatchSourceCancelHandlerEv : 192 -> 204

```
