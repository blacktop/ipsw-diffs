## RoseControllerLib

> `/System/Library/Extensions/AppleSPURose.kext/PlugIns/RoseControllerLib.plugin/RoseControllerLib`

```diff

-1014.120.3.0.0
-  __TEXT.__text: 0x8214
+1046.0.1.0.0
+  __TEXT.__text: 0x8270
   __TEXT.__auth_stubs: 0x530
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x78

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: E40B77AB-82FC-3850-9802-73605184E5E2
+  UUID: AE1046CF-C635-37C7-B318-4F9D2E4DFF7F
   Functions: 287
   Symbols:   203
   CStrings:  119
Symbols:
+ _CFAllocatorAllocateTyped
+ _CFAllocatorReallocateTyped
- _CFAllocatorAllocate
- _CFAllocatorReallocate
Functions:
~ __ZN18RoseSIKDataSession18AllocateDataBufferEPK13__CFAllocatorm : 228 -> 248
~ __ZN14RoseController5allocEPK13__CFAllocator : 64 -> 80
~ __ZN14RoseController11_getSIKInfoEPK13__CFAllocatorPPhPmj : 1360 -> 1376
~ __ZN14RoseController24QueueEventSourceCallbackEPv : 240 -> 264
~ _RoseControllerLibFactory : 164 -> 180

```
