## http

> `/System/Library/Filesystems/NetFSPlugins/http.bundle/Contents/MacOS/http`

```diff

-406.0.0.0.0
-  __TEXT.__text: 0x3ee0 sha256:475ddb4efe52f8c98a1b6b5043683720bc70dc90a729155fe8b285e4e3cb43fc
+408.0.0.0.0
+  __TEXT.__text: 0x3f08 sha256:3ec56895b1a54d65d47e63a2dbfe7202e7dc93dbc2f454f9fa4c2bcb4db634de
   __TEXT.__auth_stubs: 0x710 sha256:089825f21e19f1af5cbf93c13030492c51e3971c77d7938789436895eb857df6
   __TEXT.__cstring: 0x11f4 sha256:910997ecc4e400c4912b8c8a2ca0e13e61ee26175f768f76ea76f97228f504c8
-  __TEXT.__unwind_info: 0xc0 sha256:1a544ba0b8bde9ec71142b833f8778564b65cd20d51b384d2b48052d7c37d1f5
-  __DATA_CONST.__cfstring: 0x640 sha256:8eac7e0340f47f82c98dd7a128f77a6c3fa034f6a0bd0eadae91f43324c81e97
+  __TEXT.__unwind_info: 0xc0 sha256:3d515ec651a1b6a99341ad1e755488d888a0e05265a24b036158c42d915c1ebe
+  __DATA_CONST.__cfstring: 0x640 sha256:cfc50fafea0ec88020b14c48f83047e16338abf4db0128b637fdbd0b1a082600
   __DATA_CONST.__auth_got: 0x388 sha256:50812ae23f4ff97eae7251fed0cfbc95549b02ed38124ec2a3dd4e1f3d0daea3
   __DATA_CONST.__got: 0xe0 sha256:31a7b2fa266c87e1bd4703cdc54edf81790b05c90243ca8d89aafa5f61d64b48
   __DATA_CONST.__auth_ptr: 0x10 sha256:51b872f40f91d79303d7fee0e1be0cda96f1ad635626231b49fd9f332bb42389
-  __DATA.__data: 0x70 sha256:6816027caafb2d83fea7e15185799e9d448b24858d87079ea97d876f070f0d05
+  __DATA.__data: 0x70 sha256:13fab86dda9b977cde75ab0fef23f3a5bd259cf363a432e5e0fdfed4d98f0bc0
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
-  UUID: F420969D-1AFD-3327-85E6-1CD85E7EE52D
+  UUID: C563D24A-6D89-3F8A-93C5-69C6AEB95C40
   Functions: 25
   Symbols:   163
   CStrings:  226
Functions:
~ _percent_decode_in_place : 220 -> 236
~ _WebDAV_CreateSessionRef : sha256 069bf4a0066659e8704531482ef0b9af1deb1975af737cc4ea7c7a0f7c2fd9be -> d0c49b61e958f69145aba9815a081a6a113f022413dfc9389ccaaecca1e4789d
~ _WebDAV_GetServerInfo : sha256 7e524d65a968dde5aa260ed9716ce4f6c2662696dbbd20fdff646949ac27e864 -> d0e54b3ce4420a312dc7e17e50e2b1d43449270b0cebf725bf81dc7b7e6093ea
~ sub_c08 -> sub_c18 : sha256 9ed9dc804984f1449cf6825a622c5e65f74cf17a481fcbf2b19ff1b78ee25529 -> d7a49e47c1e72e276c688ddc409c21772cb6320bfe64163373f0b0d6a7aeac5b
~ _WebDAV_ParseURL : sha256 54b07b7237b785376bb4ec79430915f6e1358f1b6197b4eb9140300dec7c6e33 -> e8fadcd9ec5f4bb3f05c0b1766562e7c91494d6f7b6649b2b4067334fd68a587
~ _WebDAV_CreateURL : sha256 5557b2420bce0eaf62855ba211db28539aff28db22044dbbf46cb3185f3b6a13 -> a783e435f8621acb8919871bb76e8e5972986adb73ce839d4c3f7a3bb9b94210
~ _WebDAV_OpenSession : sha256 3f9f0dc457e22ddd03696ee419e43a728a665e0b0e5a76ce6a98b070f8dd2fda -> 3306336878485d868740e1af5e26f305236883f07883b2739625f74c53ff08df
~ _WebDAV_Mount : sha256 e35a05aa56f5d23b4b47019386a3c63f21c8554081c054b235165e6194ebf43b -> 25984ffa92a49461125ba7522d7ccd2ac4f6ebe0794ae535c9b666737861497d
~ sub_1aa4 -> sub_1ab4 : 3004 -> 3028
~ _WebDAV_CloseSession : sha256 306e4e892128ab0cb71d8d2e42349c246e221db9f046d4f98b7daf2a06d4ed11 -> d978318dd70ac12bacb0e3db0245561dec854a192558c64f0762fe6a479b4e5b
~ _SecCertificateCreateCFData : sha256 f4f58c74dc94fe8699167b3e879bd26ab931e226e683d292a4baf7aba5ae9806 -> 24307b7a0105ff3fada397d802ad805156dab43a962ebe01a4736f17962e7238
~ _queryForProxy : sha256 11823071e2995236301576e7a4fb3154954e363daa76d5cfe973800701c19f3a -> 8bf82db4fcfee675c78a625b336a559d3983d6b2b589450cc1a8c6fa32e0a0d4
~ _connectToServer : sha256 a09127773a6ec3674b9f6fda0cc737698b68fcde9c9f24ed8754b9194348f862 -> b82ac8ff6bfc86d31fb9b96ef8826801a8d93a18b425f0f09f7db8922da0a56a
~ sub_3ae4 -> sub_3b0c : sha256 02fe176e8506c758db8d2e40ee0293897378f4080066f0b6a3178a21708ea8ad -> b53da044acaa9ac7aa43978844e9f75d1415d101454905d083ad6d8207e06b9a
~ sub_3ce0 -> sub_3d08 : sha256 d21874875e2da5b88d0052ed3450103b9de6a218b545d4ba8d117a97ba662119 -> 96b86f69e8aa765442c8ac218536d828d583c9c75946744fc75f119470e10926
~ sub_3e38 -> sub_3e60 : sha256 a9f49ee86fb2361242906e2f81044d739b48147f704d47b717bca7f250fb2c62 -> 4579496d8a1333d14ac944362ed8f2e3ea919c090db6da1741a9fcd60552465d
~ sub_3ef0 -> sub_3f18 : sha256 4251ac2c2214480bf272b28e5501023775d58d162ec8154e148c201dc6c46d6b -> 993274857880f164eb32e22b14a62bb284bc003b905e4b615a06f8ba6280cee3
~ sub_42e0 -> sub_4308 : sha256 dff92641588e034ef6add827f33cdc58532001aa139624aa0526444fb8da8856 -> c9a41f752e65a69759af676c62af08567ecaabb50b79a289774d84e51345dff7

```
