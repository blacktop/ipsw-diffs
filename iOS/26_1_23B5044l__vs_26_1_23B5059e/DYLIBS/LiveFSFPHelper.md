## LiveFSFPHelper

> `/System/Library/PrivateFrameworks/LiveFSFPHelper.framework/LiveFSFPHelper`

```diff

-737.40.5.0.0
-  __TEXT.__text: 0x1b5bc
+737.40.13.0.0
+  __TEXT.__text: 0x1b6d4
   __TEXT.__auth_stubs: 0x730
   __TEXT.__objc_methlist: 0x1684
-  __TEXT.__const: 0x108
+  __TEXT.__const: 0x110
   __TEXT.__gcc_except_tab: 0x13e0
-  __TEXT.__oslogstring: 0x1abd
+  __TEXT.__oslogstring: 0x1b0a
   __TEXT.__cstring: 0x1739
-  __TEXT.__unwind_info: 0x7f0
+  __TEXT.__unwind_info: 0x7f8
   __TEXT.__objc_classname: 0x29a
   __TEXT.__objc_methname: 0x4023
   __TEXT.__objc_methtype: 0xf7f

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 94ED0601-741E-3CDE-B332-2C52CAF3AD1D
-  Functions: 548
-  Symbols:   2090
-  CStrings:  1239
+  UUID: 6406086B-0BEC-3CA9-979C-7D0A5B42F8F1
+  Functions: 550
+  Symbols:   2092
+  CStrings:  1240
 
Symbols:
+ ___46-[LiveFSFPItemHelper ensureFileHandleOrError:]_block_invoke_2.17.cold.2
Functions:
~ ___46-[LiveFSFPItemHelper ensureFileHandleOrError:]_block_invoke_2.17 : 420 -> 528
~ _OUTLINED_FUNCTION_6 : 12 -> 16
+ _OUTLINED_FUNCTION_7
~ ___46-[LiveFSFPItemHelper ensureFileHandleOrError:]_block_invoke_2.17.cold.1 : 136 -> 168
+ ___46-[LiveFSFPItemHelper ensureFileHandleOrError:]_block_invoke_2.17.cold.2
~ -[LiveFSFPItemHelper isHidden].cold.1 : 172 -> 164
~ -[LiveFSFPItemHelper capabilities].cold.1 : 172 -> 164
~ -[LiveFSFPItemHelper pathExtension].cold.1 : 152 -> 156
CStrings:
+ "Got non-nil NSData for attributes, but it's either malformed or empty:%lu, %p"
+ "Got success from LILookup but some out parameters are nil: %@, %@"
- "Got success from LILookup but some out parameters are null: %@, %@"

```
