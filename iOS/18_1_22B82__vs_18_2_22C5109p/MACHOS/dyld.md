## dyld

> `/usr/lib/dyld`

```diff

-1235.2.0.0.0
-  __TEXT.__text: 0x72510
-  __TEXT.__const: 0x1c70
-  __TEXT.__cstring: 0xdead
+1241.14.0.0.0
+  __TEXT.__text: 0x71c10
+  __TEXT.__const: 0x1cc0
+  __TEXT.__cstring: 0xde61
   __TEXT.__unwind_info: 0x488
   __DATA_CONST.__auth_ptr: 0x80
   __DATA_CONST.__const: 0x5668

   __DATA_DIRTY.__bss: 0x1bc0
   __DATA_DIRTY.__common: 0x1120
   __TPRO_CONST.__allocator: 0x44000
-  Functions: 2362
-  Symbols:   3253
-  CStrings:  1773
+  Functions: 2360
+  Symbols:   3250
+  CStrings:  1771
 
Symbols:
+ __Block_byref_object_copy_.164
+ __Block_byref_object_dispose_.165
+ __ZN3lsl14readPVLEUInt64ERNSt3__14spanISt4byteLm18446744073709551615EEE
+ ___ZZN5dyld412RuntimeState16setObjCNotifiersEPFvPKcPK11mach_headerEPFvS5_PvS5_PKvEPFvjPK29_dyld_objc_notify_mapped_infoEPFvSF_EPFvjSF_U13block_pointerFvjEEENK3$_0clEv_block_invoke.166
+ ___ZZN5dyld412RuntimeState16setObjCNotifiersEPFvPKcPK11mach_headerEPFvS5_PvS5_PKvEPFvjPK29_dyld_objc_notify_mapped_infoEPFvSF_EPFvjSF_U13block_pointerFvjEEENK3$_0clEv_block_invoke.166.cold.1
- _ZN5dyld412RuntimeState21initializeClosureModeEv.cold.3
- _ZN5dyld412RuntimeState21initializeClosureModeEv.cold.4
- __Block_byref_object_copy_.166
- __Block_byref_object_dispose_.167
- __ZN3lsl14readPVLEUInt64ERNSt3__14spanISt4byteLm18446744073709551615EEERy
- __ZN5dyld45Atlas5ImageD1Ev
- ___ZZN5dyld412RuntimeState16setObjCNotifiersEPFvPKcPK11mach_headerEPFvS5_PvS5_PKvEPFvjPK29_dyld_objc_notify_mapped_infoEPFvSF_EPFvjSF_U13block_pointerFvjEEENK3$_0clEv_block_invoke.168
- ___ZZN5dyld412RuntimeState16setObjCNotifiersEPFvPKcPK11mach_headerEPFvS5_PvS5_PKvEPFvjPK29_dyld_objc_notify_mapped_infoEPFvSF_EPFvjSF_U13block_pointerFvjEEENK3$_0clEv_block_invoke.168.cold.1
- __block_descriptor_tmp.163
CStrings:
+ "1241.14"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Wed Oct 16 11:12:10 PDT 2024; root:libignition-56~47467/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Wed Oct 16 11:12:10 PDT 2024; root:libignition-56~47467/libignition_core/RELEASE_ARM64E"
- "/private/var/containers/Bundle/Application/"
- "/private/var/staged_system_apps/"
- "1235.2"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Mon Oct  7 20:58:02 PDT 2024; root:libignition-56~45973/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Mon Oct  7 20:58:02 PDT 2024; root:libignition-56~45973/libignition_core/RELEASE_ARM64E"

```
