## libodaccesstoken.dylib

> `/usr/lib/libodaccesstoken.dylib`

```diff

-1003.0.1.0.0
-  __TEXT.__text: 0x29f8
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x146
-  __TEXT.__oslogstring: 0x4ba
-  __TEXT.__unwind_info: 0xe8
+1003.40.5.0.0
+  __TEXT.__text: 0x3d44
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x18c
+  __TEXT.__oslogstring: 0x990
+  __TEXT.__unwind_info: 0x120
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x70
   __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__auth_got: 0x2d0
+  __AUTH_CONST.__auth_got: 0x308
   __AUTH_CONST.__auth_ptr: 0x0
   __DATA.__bss: 0x20
   __DATA_DIRTY.__data: 0x8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/Versions/A/AppleKeyStore
   - /usr/lib/libSystem.B.dylib
-  Functions: 72
-  Symbols:   168
-  CStrings:  43
+  Functions: 96
+  Symbols:   187
+  CStrings:  67
 
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
