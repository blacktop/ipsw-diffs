## opendirectoryd

> `/usr/libexec/opendirectoryd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1003.0.1.0.0
-  __TEXT.__text: 0x5f358
-  __TEXT.__auth_stubs: 0x2080
+1003.40.5.0.0
+  __TEXT.__text: 0x60ab0
+  __TEXT.__auth_stubs: 0x20d0
   __TEXT.__objc_methlist: 0x11c
   __TEXT.__const: 0x298
-  __TEXT.__cstring: 0xc2fd
-  __TEXT.__oslogstring: 0x8c5a
+  __TEXT.__cstring: 0xc34a
+  __TEXT.__oslogstring: 0x921c
   __TEXT.__objc_methname: 0x147
   __TEXT.__objc_classname: 0x10d
   __TEXT.__objc_methtype: 0xb5
-  __TEXT.__unwind_info: 0x1d58
+  __TEXT.__unwind_info: 0x1db8
   __DATA_CONST.__const: 0x8710
-  __DATA_CONST.__cfstring: 0x8660
+  __DATA_CONST.__cfstring: 0x8680
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x1040
+  __DATA_CONST.__auth_got: 0x1068
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__auth_ptr: 0xd8
   __DATA.__objc_const: 0x1270

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsasl2.2.dylib
   - /usr/lib/libspindump.dylib
-  Functions: 1977
-  Symbols:   3375
-  CStrings:  2241
+  Functions: 2005
+  Symbols:   3388
+  CStrings:  2268
 
Symbols:
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/opendirectory/libodshared.a(constants.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/opendirectory/libodshared.a(odutils.o)
+ __copy_relative_config_path
+ _daemon_is_node_name_safe_for_path
+ _fstatat
+ _mkdirat
+ _odproplist_unlink_file_contained
+ _odproplist_write_file_contained
+ _odproplist_write_file_in_directory
+ _openat
+ _renameat
+ _unlinkat
+ odproplist_unlink_file_contained
+ odproplist_write_file_contained
+ odproplist_write_file_in_directory
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/opendirectory/libodshared.a(constants.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/opendirectory/libodshared.a(odutils.o)
CStrings:
+ "%@.plist"
+ "'%{public}@' does not name a file in a folder"
+ ".tmp.%s"
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
+ "Ignoring configuration at '%{public}@', node name '%{public}@' is not a valid node name"
+ "Path '%{public}s' is too long to write under '%{public}s'"
+ "Refusing '%{public}s' under '%{public}s', '%{public}s' is not a valid component"
+ "Refusing '%{public}s' under '%{public}s', '%{public}s' is not a valid file name"
+ "Refusing to add configuration, node name '%{public}@' is not a valid node name"
+ "Refusing to remove '%{public}@', '%{public}s' is not reachable, %{errno}d"
+ "Refusing to write absolute path '%{public}s' under '%{public}s'"
+ "com.apple.opendirectoryd.odproplist_write_file_in_directory"
+ "configuration couldn't be written, node name is invalid '%{public}@'"
```
