## SynapseSyncPlugin

> `/System/Library/Assistant/Plugins/SynapseSyncPlugin.assistantBundle/Contents/MacOS/SynapseSyncPlugin`

```diff

-3403.5.1.0.0
-  __TEXT.__text: 0x16e0
+3404.80.4.0.0
+  __TEXT.__text: 0x1744
   __TEXT.__auth_stubs: 0x100
-  __TEXT.__objc_methlist: 0xa4
+  __TEXT.__objc_methlist: 0x224
   __TEXT.__const: 0x20
   __TEXT.__cstring: 0x16f
-  __TEXT.__oslogstring: 0x440
+  __TEXT.__oslogstring: 0x41b
   __TEXT.__unwind_info: 0x78
   __TEXT.__objc_classname: 0x42
   __TEXT.__objc_methname: 0x77c

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x210
+  __DATA_CONST.__objc_selrefs: 0x2e0
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x88
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x80
-  __AUTH_CONST.__objc_const: 0x5d0
+  __AUTH_CONST.__objc_const: 0x300
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/SAObjects.framework/Versions/A/SAObjects
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2789CDEF-F728-317A-BD08-24DA33B30EE9
+  UUID: 29D45BB0-9504-3BA8-885B-628AEAF706AE
   Functions: 12
   Symbols:   40
-  CStrings:  167
+  CStrings:  168
 
Functions:
~ sub_1da262348 -> sub_1dd498360 : 1708 -> 1816
~ sub_1da262bf4 -> sub_1dd498c78 : 900 -> 908
~ sub_1da262f78 -> sub_1dd499004 : 1060 -> 1044
CStrings:
+ "%s Sync for disallowed slot=%@ is reset with validity=%@"
+ "%s ignoring reset sync for disallowed slot=%@ because serverCount=%ld"
- "%s Sync for current SlotName:%@ is reset (marked for deletion) with validity:%@\n(Next getChangeAfterAnchor log line should be 'clearing data for current SyncSlot')"

```
