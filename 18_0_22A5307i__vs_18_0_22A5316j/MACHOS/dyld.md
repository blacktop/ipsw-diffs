## dyld

> `/usr/lib/dyld`

```diff

-1228.0.0.0.0
-  __TEXT.__text: 0x718fc
+1230.3.0.0.0
+  __TEXT.__text: 0x71d7c
   __TEXT.__const: 0x1c30
-  __TEXT.__cstring: 0xddef
+  __TEXT.__cstring: 0xdead
   __TEXT.__info_plist: 0x4ee
   __TEXT.__unwind_info: 0x488
   __DATA_CONST.__auth_ptr: 0x80

   __DATA_DIRTY.__bss: 0x1bc0
   __DATA_DIRTY.__common: 0x1120
   __TPRO_CONST.__allocator: 0x44000
-  Functions: 2357
-  Symbols:   3248
-  CStrings:  1767
+  Functions: 2359
+  Symbols:   3252
+  CStrings:  1773
 
Symbols:
+ _ZN5dyld412RuntimeState21initializeClosureModeEv.cold.3
+ _ZN5dyld412RuntimeState21initializeClosureModeEv.cold.4
+ __Block_byref_object_copy_.166
+ __Block_byref_object_dispose_.167
+ __ZN3lslL17appendHexToStringIiEEvPcT_y
+ __ZN3lslL17appendHexToStringIyEEvPcT_y
+ ___ZZN5dyld412RuntimeState16setObjCNotifiersEPFvPKcPK11mach_headerEPFvS5_PvS5_PKvEPFvjPK29_dyld_objc_notify_mapped_infoEPFvSF_EPFvjSF_U13block_pointerFvjEEENK3$_0clEv_block_invoke.168
+ ___ZZN5dyld412RuntimeState16setObjCNotifiersEPFvPKcPK11mach_headerEPFvS5_PvS5_PKvEPFvjPK29_dyld_objc_notify_mapped_infoEPFvSF_EPFvjSF_U13block_pointerFvjEEENK3$_0clEv_block_invoke.168.cold.1
+ __block_descriptor_tmp.163
- __Block_byref_object_copy_.164
- __Block_byref_object_dispose_.165
- __Z10bytesToHexPKhmPc
- ___ZZN5dyld412RuntimeState16setObjCNotifiersEPFvPKcPK11mach_headerEPFvS5_PvS5_PKvEPFvjPK29_dyld_objc_notify_mapped_infoEPFvSF_EPFvjSF_U13block_pointerFvjEEENK3$_0clEv_block_invoke.166
- ___ZZN5dyld412RuntimeState16setObjCNotifiersEPFvPKcPK11mach_headerEPFvS5_PvS5_PKvEPFvjPK29_dyld_objc_notify_mapped_infoEPFvSF_EPFvjSF_U13block_pointerFvjEEENK3$_0clEv_block_invoke.166.cold.1
CStrings:
+ "\n\tRequested allgnment: 0x"
+ "\n\tRequested size: 0x"
+ "\n\tRequested target allgnment: 0x"
+ "\n\tRequested target size: 0x"
+ "\n\tkern return: 0x"
+ "/private/var/containers/Bundle/Application/"
+ "/private/var/staged_system_apps/"
+ "1230.3"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Mon Jul 15 21:20:53 PDT 2024; root:libignition-56~33984/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Mon Jul 15 21:20:53 PDT 2024; root:libignition-56~33984/libignition_core/RELEASE_ARM64E"
- " bytes (kr: 0x"
- "1228"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Wed Jul  3 20:32:44 PDT 2024; root:libignition-56~31680/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Wed Jul  3 20:32:44 PDT 2024; root:libignition-56~31680/libignition_core/RELEASE_ARM64E"

```
