## opendirectoryd

> `/usr/libexec/opendirectoryd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1003.0.1.0.0
-  __TEXT.__text: 0x5f358
+1003.40.4.0.0
+  __TEXT.__text: 0x5f3a4
   __TEXT.__auth_stubs: 0x2080
   __TEXT.__objc_methlist: 0x11c
   __TEXT.__const: 0x298
Symbols:
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/opendirectory/libodshared.a(constants.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/opendirectory/libodshared.a(odutils.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/opendirectory/libodshared.a(constants.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/opendirectory/libodshared.a(odutils.o)
Functions:
~ _odrequesttype_for_name : 204 -> 208
~ __odrequest_rpc_deserialize : 212 -> 284
```
