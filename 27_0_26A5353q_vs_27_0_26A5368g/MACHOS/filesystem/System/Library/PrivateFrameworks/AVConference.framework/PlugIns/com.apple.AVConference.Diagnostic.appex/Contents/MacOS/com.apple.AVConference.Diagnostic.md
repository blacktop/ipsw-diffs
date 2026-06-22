## com.apple.AVConference.Diagnostic

> `/System/Library/PrivateFrameworks/AVConference.framework/PlugIns/com.apple.AVConference.Diagnostic.appex/Contents/MacOS/com.apple.AVConference.Diagnostic`

```diff

-2235.48.1.0.0
-  __TEXT.__text: 0x11d4 sha256:deebb4cb994fabbda3cd316791d6aca1861d3738a17808d4972ff556cefaa434
+2235.52.1.0.0
+  __TEXT.__text: 0x11d0 sha256:fd5fddf6e494b03cc96718f5c8972f45d3f41545ad89c81e2ab0762f8935eb92
   __TEXT.__auth_stubs: 0x110 sha256:01ceb470dab9b3fef3bea976c50add594ba44aaeb6ffee2230251be0dab6e0ae
   __TEXT.__objc_stubs: 0x520 sha256:c24993b07cda043bc798e27046b392111e4ad38e0d8e63a87c0693147ef0f4ca
-  __TEXT.__objc_methlist: 0xb0 sha256:749aee53c6af8e3fedefdbb7f9aa9a741145c71c7b01c4e7a668667d0e8dd610
+  __TEXT.__objc_methlist: 0xb0 sha256:ce53a3ae48972fadbc572d63683c3395ae1fa7f8b8cb80d6a0afb6bf8a6144a2
   __TEXT.__const: 0x88 sha256:a9f50d82ac9235f5936120a703f7c51188b92bd09410284ceacdd071ffa8be96
   __TEXT.__cstring: 0x251 sha256:31bd71e3bf6e7c7fd5b3ba1b15b9a4d1447a578cdc673e5dd82547ab5ba9f344
   __TEXT.__oslogstring: 0x3c1 sha256:d3fa08ea911f4530afedd7b1de8a6af26ba2a2b5d7821e8558d2e65b50829c0a
   __TEXT.__objc_classname: 0x2b sha256:551da86c59a296cc2d976c5e05c316ab5a478e67d161f7c2962b6a36e7cf535f
   __TEXT.__objc_methname: 0x428 sha256:5754da7a46fe6325c3eadef900118ca26f27c59e459580b5f5bd1211953205eb
   __TEXT.__objc_methtype: 0x55 sha256:70ad46dac6564f96d61257800567ad352cb61756b33bd0d33395513437d38990
-  __TEXT.__unwind_info: 0x98 sha256:35bcad073e4cea9fdeb0597bb0733bbd3fe046fb7bbe96d6beed0c1870ea8987
-  __DATA_CONST.__const: 0x40 sha256:d171f9c09f1f2d8027538debf85970c0729f13a2f324253e863b051187e6d93c
+  __TEXT.__unwind_info: 0x98 sha256:da092e9c932651151186bce697e1af3fbec8cd51cbcd2a81e8425f8b310ee37c
+  __DATA_CONST.__const: 0x40 sha256:12604fb8de0761e3bb118c3a89b3ab799089f5d999124f7e1596850ad9e79f3f
   __DATA_CONST.__cfstring: 0x320 sha256:01c61f36d870b4f7e407e4ec6cec2b66ee74c253474db76cb4247850eebbdb02
   __DATA_CONST.__objc_classlist: 0x8 sha256:2f6e240d650a1ce947cba459a48032ba4361bdb2191be041d9738ad33812126e
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 028DA595-B235-363B-83F5-C607275B1ADD
+  UUID: 80048F76-7CA6-3CC8-8AD5-63B68875A31C
   Functions: 20
   Symbols:   113
   CStrings:  117
Functions:
~ +[com_apple_AVConference_DiagnosticExtension defaultSpindumpPath] : sha256 f73e602781036544f3a99f33ba1f994ee724f2750df8ab8686f64d54096d5799 -> 91be2bf7e88f5af24e78f0bb38648076105d195da20a3cbbcd076d0bc24c5ea4
~ +[com_apple_AVConference_DiagnosticExtension defaultAVConferenceCachePath] : sha256 ff1f28890749f962326a6aaac14ac702989dbcc996e68a06fc88e8c47fb2ef14 -> 548d18deb16aeee9eb14310edfebb05899c232ca8bb6ec808a20e8f91478f052
~ +[com_apple_AVConference_DiagnosticExtension realHomeDirectory] : sha256 300503c33bb1352c194df95fdd07eb5454f1135af7b510fbf1d9cf75ada9a417 -> 3765f17d35434a1501d274d7653b18d98a3cff9eac44e6f79daddd436c170962
~ -[com_apple_AVConference_DiagnosticExtension copyDirectory:withPredicate:toSubDirectory:] : 928 -> 924
~ -[com_apple_AVConference_DiagnosticExtension copyFile:withPredicate:toSaveDirectory:] : sha256 73379e8df01986c431f65a89c4df07f113aeb6f18d707cc401d8eaf290c413e2 -> a192db62930d8592960ed6ecdddfb0c719c5690fb25ef9dc1981bef312c191c2
~ -[com_apple_AVConference_DiagnosticExtension copyStackshotsAndCrashes] : sha256 311fb727e136adc2327e6e845d02335fef0ef8d1d8aa8638d0eda04870cca2d5 -> b9c3eb045dddccaa3c27b11394b61552750afacf593b768f90fd49f898f07d7a
~ -[com_apple_AVConference_DiagnosticExtension copySpindumps] : sha256 51b42f34da7e16de56052643179b5757127d91c72710907a7a362baa5815c745 -> 77efa6efe142948166cb9497e48e1c0997b3a374f647a2e5b279fef5872c3178
~ -[com_apple_AVConference_DiagnosticExtension copyDumps] : sha256 3712271c982aa42f0778cf81399a412b2df93ea8c20623e3e36a30444b690cb6 -> ca599b13bd6ea93fd23b30e73ad9ed6e96f74dcf1a3c7b304b88d5407dbefde8
~ -[com_apple_AVConference_DiagnosticExtension copyRTCReporting] : sha256 f96265ece6fd57f20231c5d3044d439597dd5a15e13dfbff8d6e55411a04c823 -> d2dd01fac09c76e161b86d4d00a421c69b6e8dfad3e60a2cb0bddd3a4b0568b7
~ -[com_apple_AVConference_DiagnosticExtension attachmentsForParameters:withProgressHandler:] : sha256 00ab9b0a2a2f3cf32f240b822bba87d2bc1f9538466231bdfa37e381b86397c3 -> 54ccc1d05c2513883484fb03a8dee3323801f7286674de43f9ef42295444a3e6
~ __89-[com_apple_AVConference_DiagnosticExtension copyDirectory:withPredicate:toSubDirectory:]_block_invoke.cold.1 : sha256 cd30774a1087947f41e23d7f637cc2e53db7410a3a90c29242923c0d5354a9dc -> 9d6315bf894689d111fe1ad307eae6035aeeacd7783b3988bba9c4d884289fa0
~ -[com_apple_AVConference_DiagnosticExtension copyFile:withPredicate:toSaveDirectory:].cold.1 : sha256 dc6188b9ff6ee1f4ba81b3f483f8ae99c4844ad4a6c2668f8a7d02d1d9161555 -> 8f1131242569b3a577a2f8366f20a934e589b30aacf8e7bda3c02f90d9dabe19

```
