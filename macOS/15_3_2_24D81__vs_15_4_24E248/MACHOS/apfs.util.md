## apfs.util

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs.util`

```diff

-2317.81.2.0.0
-  __TEXT.__text: 0x2c04
+2332.101.1.0.0
+  __TEXT.__text: 0x2c1c
   __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__cstring: 0x1b96
-  __TEXT.__const: 0x10
-  __TEXT.__unwind_info: 0x90
+  __TEXT.__cstring: 0x1ba5
+  __TEXT.__const: 0x40
+  __TEXT.__unwind_info: 0x88
   __DATA_CONST.__auth_got: 0x178
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x68

   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: E57AEBDB-367C-331E-9C60-A3F5D934569F
+  UUID: 37E71D2B-C4C2-3EA5-99D8-AFC254FC208B
   Functions: 21
   Symbols:   56
-  CStrings:  178
+  CStrings:  179
 
Functions:
~ sub_1000036b4 -> sub_1000009c4 : 3864 -> 3848
~ sub_100004e7c -> sub_10000217c : 316 -> 328
~ sub_100005124 -> sub_100002430 : 832 -> 916
~ sub_100005688 -> sub_1000029e8 : 936 -> 960
~ sub_100005a30 -> sub_100002da8 : 1700 -> 1620
CStrings:
+ "-fixup"
+ "Failed to mark %s as purgeable, errno: %d (%s) (flags 0x%llx supplemental 0x%llx)\n"
- "Failed to mark %s as purgeable %d (%s) (flags 0x%llx supplemental 0x%llx)\n"

```
