## NetworkUplinkClock

> `/System/Library/Audio/Plug-Ins/HAL/NetworkUplinkClock.driver/NetworkUplinkClock`

```diff

-1075.0.0.0.0
-  __TEXT.__text: 0x9af4 sha256:348d68c10fe70089e46253aed44d0a884847cb5ba82ce1c21fa4f37b9fcb0f94
-  __TEXT.__auth_stubs: 0x5a0 sha256:b447092adef5d60a6fbe67310029eb96bb154d70aa0b37a05bad55f443365ab9
+1158.0.0.0.0
+  __TEXT.__text: 0x9398 sha256:4d0e762e989556e783d37730dedcb43f6a900566c4e563c08349b1340616991d
+  __TEXT.__auth_stubs: 0x590 sha256:0d9df83f76a774fdfdc6c24c7f0fe9482c6f4d500123e32a432ca0d3a365b6ae
   __TEXT.__const: 0x1f1 sha256:9ca5bfab7aa2453766ec1d64e753caf164b0b784d708763328b1906ce7eb15be
-  __TEXT.__gcc_except_tab: 0x820 sha256:5785e0884cd11dffe994515bab506e13ad02440a6ae7381e11f584ff34563a46
-  __TEXT.__oslogstring: 0x6bf sha256:7f712387bffeac1a08d6ac3e676577208d7d379f46d4e2f0113d1a3ce72e71b8
-  __TEXT.__cstring: 0x69c sha256:b51ffe03bda7af8cfb7c14fc47e84ef552e629069d88162c4147214a497e3366
-  __TEXT.__unwind_info: 0x3d8 sha256:a386d5dc50d1657d064aa6fedfbac197755497971359738d3607b6f4b6c56a33
-  __DATA_CONST.__auth_got: 0x2d8 sha256:a04d2701ec17dab4451b1e4a16ee55945e97d371f318883be85e497a83eb4794
-  __DATA_CONST.__got: 0x70 sha256:eeb4a875962754689ae39c3b0bbbe41acda2cd6044da37926026fea1012b48cd
-  __DATA_CONST.__const: 0x320 sha256:1c6e4840a79b87a4ca408317c49b6e16fba48a60d7018110b88a3965488817c9
-  __DATA_CONST.__cfstring: 0x4e0 sha256:3bd9f2d880c99a1396540711a66d1282e435cb116686d5ab942aee14ff5a80bb
-  __DATA.__data: 0x148 sha256:ee5989775802f8a121dd750f10f1f5e755cb2be83213eee7ea64529a27068935
-  __DATA.__bss: 0x41 sha256:98ce42deef51d40269d542f5314bef2c7468d401ad5d85168bfab4c0108f75f7
+  __TEXT.__gcc_except_tab: 0x738 sha256:d3f12894343999edb31038bc01c42e784f171be29fbcf85cdc2eb03674214d72
+  __TEXT.__oslogstring: 0x6bf sha256:b44c6fde797348d209d8d19c0b4b3b9d7e2b343342488f0fe4b817a7f36a77d9
+  __TEXT.__cstring: 0x67c sha256:20f0102cefb9fa9543aa41dca01cfe14a1a19e3324c8cccdbfe8315abb29db22
+  __TEXT.__unwind_info: 0x390 sha256:fd6c4b472b38b930233392135a8a6b9709903c1125fbcb6aeb1674c9651fb61a
+  __DATA_CONST.__const: 0x2e0 sha256:a30c3bcda1d61d5de285440746b9771e786a6d5e88a0535a78c3a0f8f82b4901
+  __DATA_CONST.__cfstring: 0x4e0 sha256:836223b21ae1cb90569f6f8dbe753ff53ef43df69fd5dff3a717cddb8c87d853
+  __DATA_CONST.__auth_got: 0x2d0 sha256:5ebc0d77364fdef00d8ae0f3968d62be6229292416b7de45754f3275e98c8759
+  __DATA_CONST.__got: 0x70 sha256:9a9bec6a08467c4649e9addc2b27261401f5433388ec08e5ff7b84b2097ff9cd
+  __DATA.__data: 0x148 sha256:3f5eaf7d31d957a5cce2a463b1c52644638439fc96573a789337107cce08ebf9
+  __DATA.__bss: 0x31 sha256:78877fa898f0b4c45c9c33ae941e40617ad7c8657a307db62bc5691f92f4f60e
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/PrivateFrameworks/AppleSauce.framework/AppleSauce

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libWirelessAudioIPC.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 93B680DC-3609-3C68-8FE7-4BF56457EF5A
-  Functions: 125
-  Symbols:   112
-  CStrings:  202
+  UUID: 9BCB1D7D-2984-3252-B90A-DB985DBF5193
+  Functions: 122
+  Symbols:   111
+  CStrings:  201
 
Symbols:
- _os_parse_boot_arg_int
CStrings:
+ "TimeSource %{multichar}x"
+ "changing time source %{multichar}x -> %{multichar}x (running %u)"
+ "failed %{multichar}x"
+ "object %u, selector %{multichar}x, scope %{multichar}x, element %u"
+ "op %{multichar}x"
+ "result %{multichar}x"
+ "result %{multichar}x, changed %zu"
+ "result %{multichar}x, dataSize %u"
+ "result %{multichar}x, isSettable %{BOOL}d"
+ "result %{multichar}x, sampleTime %lf, hostTime %llu, seed %llu"
+ "success %{multichar}x"
+ "unsupported time source %{multichar}x"
- "TimeSource %{waipc:4cc}u"
- "changing time source %{waipc:4cc}u -> %{waipc:4cc}u (running %u)"
- "dale-ignore-time-sync-interrupt"
- "failed %{waipc:4cc}u"
- "object %u, selector %{waipc:4cc}u, scope %{waipc:4cc}u, element %u"
- "op %{waipc:4cc}u"
- "result %{waipc:4cc}u"
- "result %{waipc:4cc}u, changed %zu"
- "result %{waipc:4cc}u, dataSize %u"
- "result %{waipc:4cc}u, isSettable %{BOOL}d"
- "result %{waipc:4cc}u, sampleTime %lf, hostTime %llu, seed %llu"
- "success %{waipc:4cc}u"
- "unsupported time source %{waipc:4cc}u"

```
