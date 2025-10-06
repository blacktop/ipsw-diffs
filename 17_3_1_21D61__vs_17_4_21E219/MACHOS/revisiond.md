## revisiond

> `/System/Library/PrivateFrameworks/GenerationalStorage.framework/revisiond`

```diff

-362.0.0.0.0
-  __TEXT.__text: 0x2c96c
-  __TEXT.__auth_stubs: 0xf10
-  __TEXT.__objc_stubs: 0x31e0
+365.100.2.0.0
+  __TEXT.__text: 0x2cf30
+  __TEXT.__auth_stubs: 0xf20
+  __TEXT.__objc_stubs: 0x3260
   __TEXT.__objc_methlist: 0xf90
   __TEXT.__const: 0x1a8
-  __TEXT.__gcc_except_tab: 0x450
-  __TEXT.__cstring: 0x4a21
-  __TEXT.__objc_methname: 0x3808
-  __TEXT.__oslogstring: 0x26f3
+  __TEXT.__gcc_except_tab: 0x468
+  __TEXT.__cstring: 0x4a52
+  __TEXT.__objc_methname: 0x3874
+  __TEXT.__oslogstring: 0x27ec
   __TEXT.__objc_classname: 0x1a7
   __TEXT.__objc_methtype: 0x1261
-  __TEXT.__unwind_info: 0x878
-  __DATA_CONST.__auth_got: 0x798
+  __TEXT.__unwind_info: 0x8a0
+  __DATA_CONST.__auth_got: 0x7a0
   __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0xf10
-  __DATA_CONST.__cfstring: 0x2500
+  __DATA_CONST.__const: 0xf60
+  __DATA_CONST.__cfstring: 0x2520
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x138
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x3300
-  __DATA.__objc_selrefs: 0xef8
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x190
-  __DATA.__objc_superrefs: 0x70
+  __DATA.__objc_selrefs: 0xf18
   __DATA.__objc_ivar: 0x1a0
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x490

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A7F0D11B-0051-3AA4-A9B4-5D56024745CD
-  Functions: 1008
-  Symbols:   332
-  CStrings:  1807
+  UUID: 7F5E747C-EE8D-3D98-9858-41689CC15CAA
+  Functions: 1017
+  Symbols:   335
+  CStrings:  1819
 
Symbols:
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSFileHandle
+ _SANDBOX_CHECK_CANONICAL
+ _realpath$DARWIN_EXTSN
- _NSFileModificationDate
CStrings:
+ "21:24:35"
+ "B16@?0@\"NSURL\"8"
+ "Feb 16 2024"
+ "Invalid cookie URL"
+ "Invalid volume URL"
+ "T@\"NSString\",?,R,C"
+ "Unknown error. See logs for more details."
+ "[DEBUG] [ImportCookie] Clearing cookie."
+ "[DEBUG] [ImportCookie] No permission."
+ "[ERROR] [ImportCookie] Cant open cookie path, errno %s"
+ "[ERROR] [ImportCookie] Couldn't lstat volume  %@, error: %s"
+ "[ERROR] [ImportCookie] Found error while clearing cookie, error: %@."
+ "[ERROR] [ImportCookie] Found error while opening cookie, error: %@."
+ "[ERROR] [ImportCookie] Found error while writing cookie, error: %@."
+ "[ERROR] [ImportCookie] Unable to open cookie path inside library: %@, errno %s"
+ "[ERROR] [ImportCookie] Unable to open cookie path, error %s"
+ "[ERROR] [ImportCookie] unable to get volume real path."
+ "distantPast"
+ "i36@0:8@16B24^@28"
+ "importCookieFileDescriptorForVolumeURL:forWriting:error:"
+ "initWithFileDescriptor:closeOnDealloc:"
+ "offsetInFile"
+ "readDataToEndOfFileAndReturnError:"
+ "truncateAtOffset:error:"
+ "writeData:error:"
- "18:30:46"
- "@36@0:8@16B24^@28"
- "Could not read cookie."
- "Could not write cookie."
- "Dec 20 2023"
- "[DEBUG] [ImportCookie] Deleting cookie."
- "[DEBUG] [ImportCookie] No cookie to delete."
- "[DEBUG] [ImportCookie] Unable to find a cookie file for Volume: %@"
- "[ERROR] [ImportCookie] Couldn't lstat volume  %@"
- "[ERROR] [ImportCookie] Found error while removing cookie %@, error: %@."
- "[ERROR] [ImportCookie] Found error while writing cookie %@, error: %@."
- "dataWithContentsOfFile:options:error:"
- "importCookieURLForVolumeURL:forWriting:error:"
- "writeToFile:options:error:"

```
