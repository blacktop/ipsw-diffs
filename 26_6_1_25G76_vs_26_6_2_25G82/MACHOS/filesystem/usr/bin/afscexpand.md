## afscexpand

> `/usr/bin/afscexpand`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

 174.160.2.0.0
-  __TEXT.__text: 0x13de8
+  __TEXT.__text: 0x13df8
   __TEXT.__auth_stubs: 0x320
   __TEXT.__const: 0x235a0
   __TEXT.__cstring: 0xbca
Functions:
~ sub_1000110f4 : 2204 -> 2220
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.MZtLay/Sources/AppleFSCompression_executables/Common/ChunkCompression.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.MZtLay/Sources/AppleFSCompression_executables/Common/commonUtilsUser.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.MZtLay/Sources/AppleFSCompression_executables/Libraries/CompressData/CompressData.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hBXq91/Sources/AppleFSCompression_executables/Common/ChunkCompression.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hBXq91/Sources/AppleFSCompression_executables/Common/commonUtilsUser.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hBXq91/Sources/AppleFSCompression_executables/Libraries/CompressData/CompressData.c"
```
