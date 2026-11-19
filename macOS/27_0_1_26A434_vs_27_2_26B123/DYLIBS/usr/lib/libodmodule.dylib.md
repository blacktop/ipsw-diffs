## libodmodule.dylib

> `/usr/lib/libodmodule.dylib`

```diff

-1003.0.1.0.0
-  __TEXT.__text: 0x8eb8
+1003.40.5.0.0
+  __TEXT.__text: 0xa210
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x372d
-  __TEXT.__oslogstring: 0x25f
-  __TEXT.__unwind_info: 0x278
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0x3773
+  __TEXT.__oslogstring: 0x735
+  __TEXT.__unwind_info: 0x2a8
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0

   __AUTH_CONST.__const: 0x730
   __AUTH_CONST.__cfstring: 0x32e0
   __AUTH_CONST.__objc_const: 0xc40
-  __AUTH_CONST.__auth_got: 0x4b8
+  __AUTH_CONST.__auth_got: 0x4f0
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x370
   __DATA.__data: 0x7c8

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 226
-  Symbols:   991
-  CStrings:  527
+  Functions: 251
+  Symbols:   1010
+  CStrings:  551
 
Symbols:
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _fstatat
+ _mkdirat
+ _odproplist_unlink_file_contained
+ _odproplist_write_file_contained
+ _odproplist_write_file_in_directory
+ _openat
+ _renameat
+ _snprintf
+ _stat
+ _unlinkat
+ odproplist_unlink_file_contained
+ odproplist_write_file_contained
+ odproplist_write_file_in_directory
CStrings:
+ "'%{public}@' does not name a file in a folder"
+ ".tmp.%s"
+ "/"
+ "Cannot remove a file without a path"
+ "Cannot write a property list without a path"
+ "Cannot write a property list without both a folder and a path"
+ "Failed to create '%{public}s' under '%{public}s' %{errno}d"
+ "Failed to create '%{public}s' under '%{public}s', %{errno}d"
+ "Failed to create a CFString for '%{public}s'"
+ "Failed to open '%{public}s' %{errno}d"
+ "Failed to open '%{public}s' under '%{public}s' %{errno}d"
+ "Failed to remove '%{public}s' from '%{public}s' %{errno}d"
+ "Failed to rename '%{public}s' to '%{public}s' under '%{public}s' %{errno}d"
+ "Failed to retrieve file name from CFString %{public}@"
+ "Failed to retrieve path from CFString %{public}@"
+ "Failed to write '%{public}s' under '%{public}s' %{errno}d"
+ "File name '%{public}s' is too long to write under '%{public}s'"
+ "File name '%{public}s' leaves no room for the .tmp. prefix under '%{public}s'"
+ "Path '%{public}s' is too long to write under '%{public}s'"
+ "Refusing '%{public}s' under '%{public}s', '%{public}s' is not a valid component"
+ "Refusing '%{public}s' under '%{public}s', '%{public}s' is not a valid file name"
+ "Refusing to remove '%{public}@', '%{public}s' is not reachable, %{errno}d"
+ "Refusing to write absolute path '%{public}s' under '%{public}s'"
+ "com.apple.opendirectoryd.odproplist_write_file_in_directory"
```
