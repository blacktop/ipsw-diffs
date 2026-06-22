## pthread_kasan

> `/System/KernelKit/System/Library/Extensions/pthread.kext/pthread_kasan`

```diff

 553.0.0.0.0
   __TEXT.__cstring: 0x72d sha256:7d8ccfb8101d1b0ce701e4a491856d1fbcd49d78221673a24272c5a031975bc9
-  __TEXT_EXEC.__text: 0x8e8c sha256:a66334c82d5d85334c78ec4ed3ad356d3d068ac96a8b20eb0ac9fa75b3e52d20
-  __TEXT_EXEC.__auth_stubs: 0x440 sha256:a99dcf2374071b0e9192d3e66e0b443c851d3fd7ac5b09f02837d4470b24c95c
-  __DATA.__data: 0x160 sha256:f05fd086964eb3a817b4251c7f60d9656e36263e285f20f483bf61480c73b6a5
+  __TEXT_EXEC.__text: 0x8d38 sha256:433a1f6f9065b59f45e7fc91193dba74546315bc9e99b927f799b52d23dd10fe
+  __TEXT_EXEC.__auth_stubs: 0x440 sha256:2a2de13ad7a22732e2f3d176d06ec1a2b63b2b6efc947060f6fdabc5b2dc45f7
+  __DATA.__data: 0x148 sha256:fffd55696c7e0eb8759d6549ce0d323583256601963280639a60f65d5b0681d2
   __DATA.__bss: 0x21 sha256:7f9c9e31ac8256ca2f258583df262dbc7d6f68f2a03043d5c99a4ae5a7396ce9
   __DATA.__common: 0x30 sha256:17b0761f87b081d5cf10757ccc89f12be355c70e2e29df288b65b30710dcbcd1
-  __DATA_CONST.__const: 0x3f8 sha256:4c76060efc57548a3ebf5cc40cb44f610d22fe6ea6203737612ffc3e4d0b9fe9
-  __DATA_CONST.__weak_got: 0x10 sha256:b4889b61c70a86372363d8e740ca1e394432a2c5bd5f248f0ecc1da5f9db0b4b
+  __DATA_CONST.__const: 0x3f8 sha256:1fc56b70a8b10e507179e897c9c8a23e4cee50ca64e3fdbc376a8f2b9ec9ec87
+  __DATA_CONST.__weak_got: 0x8 sha256:4d5e4a89e282aa9c5a6e8653d829beb09c63ba02193d0e40ef06ebe7c2850f35
   __DATA_CONST.__kalloc_type: 0x80 sha256:0d966ee39a17a91db37a174b54c14ba7d35a37c78b5c64b7abd9ccc36a4e6beb
-  __DATA_CONST.__auth_got: 0x220 sha256:97de900a51f3e5c847384904e9c1d1ae872a9154fe22ec8ea11add571725220f
-  __DATA_CONST.__got: 0x18 sha256:0e924264bd8a6114f5393b1d9b367d054e6705f688ead6ab3b2f826a868b3143
-  UUID: 53455330-B32C-3E92-86F6-C841414BE2F7
-  Functions: 149
-  Symbols:   859
+  __DATA_CONST.__auth_got: 0x220 sha256:27c373f32a08abdd9f6ff129731cff8388310e7490d1db46770b186b040fb8fe
+  __DATA_CONST.__got: 0x18 sha256:8d80b88767e4fcb6cde0d44ad0d8581fb1114c5d0ca372286e4d6541a1219dbe
+  UUID: 674D1E5E-ED0B-30DD-AF53-1EC198A6AF8C
+  Functions: 147
+  Symbols:   847
   CStrings:  42
 
Symbols:
+ /AppleInternal/Library/BuildRoots/4~CR6nugD_X0kQ5KObqE8qQnifOR7ebWSp-C4Z5NM/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/DerivedSources/
+ /AppleInternal/Library/BuildRoots/4~CR6nugD_X0kQ5KObqE8qQnifOR7ebWSp-C4Z5NM/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_init.o
+ /AppleInternal/Library/BuildRoots/4~CR6nugD_X0kQ5KObqE8qQnifOR7ebWSp-C4Z5NM/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_support-33476a9867ed3d52621062a6ee74c8aa.o
+ /AppleInternal/Library/BuildRoots/4~CR6nugD_X0kQ5KObqE8qQnifOR7ebWSp-C4Z5NM/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_support-6ce9755f0db02bbfc0a7816b88dd7ed5.o
+ /AppleInternal/Library/BuildRoots/4~CR6nugD_X0kQ5KObqE8qQnifOR7ebWSp-C4Z5NM/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_synch.o
+ /AppleInternal/Library/BuildRoots/4~CR6nugD_X0kQ5KObqE8qQnifOR7ebWSp-C4Z5NM/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/pthread.swiftmodule
+ /AppleInternal/Library/BuildRoots/4~CR6nugD_X0kQ5KObqE8qQnifOR7ebWSp-C4Z5NM/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/pthread_info.o
+ /AppleInternal/Library/BuildRoots/4~CR6nugD_X0kQ5KObqE8qQnifOR7ebWSp-C4Z5NM/Library/Caches/com.apple.xbs/TemporaryDirectory.LFv4pp/Sources/libpthread_kernelkit/kern/
+ _$es12MetadataKindO8metadataABSgSV_tcfCTf4nd_n
+ _$es29ExistentialTypeRepresentationO7projectySV8metadata_SV5valuetSVF
+ _$es7tryCast33_8BFEAB69C69C8B87ED137407D82370D4LL3dst0J8Metadata3src0lK013takeOnSuccesss07DynamicB6ResultABLLOSv_S3VSbtF
+ __swift_embedded_metadata_destroy
+ __swift_embedded_metadata_get_vwt_flags
- /AppleInternal/Library/BuildRoots/4~CQdZugDmK-TBX8cihp3H-DsuD_DWHvbu0riEYc8/Library/Caches/com.apple.xbs/TemporaryDirectory.dlaqW0/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/DerivedSources/
- /AppleInternal/Library/BuildRoots/4~CQdZugDmK-TBX8cihp3H-DsuD_DWHvbu0riEYc8/Library/Caches/com.apple.xbs/TemporaryDirectory.dlaqW0/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_init.o
- /AppleInternal/Library/BuildRoots/4~CQdZugDmK-TBX8cihp3H-DsuD_DWHvbu0riEYc8/Library/Caches/com.apple.xbs/TemporaryDirectory.dlaqW0/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_support-32e3cb029c2dcf87b5b6fbbac751a1de.o
- /AppleInternal/Library/BuildRoots/4~CQdZugDmK-TBX8cihp3H-DsuD_DWHvbu0riEYc8/Library/Caches/com.apple.xbs/TemporaryDirectory.dlaqW0/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_support-3a806cb804712b7182e06f72c9921000.o
- /AppleInternal/Library/BuildRoots/4~CQdZugDmK-TBX8cihp3H-DsuD_DWHvbu0riEYc8/Library/Caches/com.apple.xbs/TemporaryDirectory.dlaqW0/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/kern_synch.o
- /AppleInternal/Library/BuildRoots/4~CQdZugDmK-TBX8cihp3H-DsuD_DWHvbu0riEYc8/Library/Caches/com.apple.xbs/TemporaryDirectory.dlaqW0/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/pthread.swiftmodule
- /AppleInternal/Library/BuildRoots/4~CQdZugDmK-TBX8cihp3H-DsuD_DWHvbu0riEYc8/Library/Caches/com.apple.xbs/TemporaryDirectory.dlaqW0/Binaries/libpthread_kernelkit/install/TempContent/Objects/libpthread.build/pthread kext.build/Objects-kasan/arm64e/pthread_info.o
- /AppleInternal/Library/BuildRoots/4~CQdZugDmK-TBX8cihp3H-DsuD_DWHvbu0riEYc8/Library/Caches/com.apple.xbs/TemporaryDirectory.dlaqW0/Sources/libpthread_kernelkit/kern/
- __swift_embedded_error_metadata_storage
- __swift_embedded_existential_destroy
- __swift_embedded_existential_init_with_copy
- __swift_embedded_existential_init_with_take
- __swift_embedded_invoke_box_destroy
- __swift_embedded_invoke_heap_object_destroy
- _swift_release
- _swift_releaseBox

```
