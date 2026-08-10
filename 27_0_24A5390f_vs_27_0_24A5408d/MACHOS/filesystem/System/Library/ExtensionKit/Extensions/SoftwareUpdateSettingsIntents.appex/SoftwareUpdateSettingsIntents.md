## SoftwareUpdateSettingsIntents

> `/System/Library/ExtensionKit/Extensions/SoftwareUpdateSettingsIntents.appex/SoftwareUpdateSettingsIntents`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_entry`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-772.0.10.0.0
-  __TEXT.__text: 0x17900
+772.0.20.0.0
+  __TEXT.__text: 0x180cc
   __TEXT.__auth_stubs: 0xe10
   __TEXT.__objc_stubs: 0x360
-  __TEXT.__const: 0x2944
+  __TEXT.__const: 0x2954
   __TEXT.__swift5_typeref: 0xd56
   __TEXT.__swift5_reflstr: 0x383
   __TEXT.__swift5_assocty: 0x360
   __TEXT.__constg_swiftt: 0x500
   __TEXT.__swift5_fieldmd: 0x2c4
-  __TEXT.__cstring: 0x1235
-  __TEXT.__oslogstring: 0x6b8
+  __TEXT.__cstring: 0x1375
+  __TEXT.__oslogstring: 0x850
   __TEXT.__swift5_proto: 0x1bc
   __TEXT.__swift5_types: 0x6c
   __TEXT.__swift_as_entry: 0x7c

   __TEXT.__objc_methtype: 0x77
   __TEXT.__swift5_capture: 0x14
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x878
+  __TEXT.__unwind_info: 0x888
   __TEXT.__eh_frame: 0x7b0
   __DATA_CONST.__const: 0x7d0
   __DATA_CONST.__objc_classlist: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 654
+  Functions: 656
   Symbols:   128
-  CStrings:  153
+  CStrings:  160
 
Symbols:
+ _swift_bridgeObjectRelease_n
- _objc_retain_x28
CStrings:
+ "Apple Beta Software Program or Apple Developer Program"
+ "Beta Updates under Settings → General → Software Update"
+ "Finished to scan for update with results: %{public}s"
+ "General → Software Update"
+ "Intent getting the value of the Automatic Security Response Install: %{bool,public}d"
+ "Intent getting the value of the OS Automatic Download: %{bool,public}d"
+ "Intent setting the value of the Automatic Security Response Install to: %{bool,public}d"
+ "Intent setting the value of the OS Automatic Download to: %{bool,public}d"
+ "Open Software Update Settings"
+ "Perform Software Update Now"
+ "Perform Software Update Now under Settings → General → Software Update"
+ "Perform Software Update Tonight"
+ "Perform Software Update Tonight under Settings → General → Software Update"
+ "SUSettings Intents got SU Scan Results. Error: %{public}@; results: %{public}@"
+ "Software Update under Settings → General"
+ "The Apple Beta Software Program or Apple Developer Program available setting"
+ "developer update"
+ "developer updates"
+ "🐞 %{public}s | %{public}s | line:%{public}ld => Auto update turned off by user request"
+ "🐞 %{public}s | %{public}s | line:%{public}ld => Auto update turned on by user request"
+ "🐞 %{public}s | %{public}s | line:%{public}ld => Finished to refreshBetaUpdates"
+ "🐞 %{public}s | %{public}s | line:%{public}ld => Perform called with property value: %{bool,public}d"
+ "🐞 %{public}s | %{public}s | line:%{public}ld => Starting to refreshBetaUpdates"
+ "🐞 %{public}s | %{public}s | line:%{public}ld => Unable to create SUManagerClient instance"
+ "🐞 %{public}s | %{public}s | line:%{public}ld => Unable to create SUSettingsStatefulUIManager"
+ "🐞 %{public}s | %{public}s | line:%{public}ld => Unable to init SUManagerClient"
+ "🐞 %{public}s | %{public}s | line:%{public}ld => User approved turning off the auto update"
+ "🐞 %{public}s | %{public}s | line:%{public}ld => User needs to approved turning off the auto update since there is a scheduled update"
+ "🐞 %{public}s | %{public}s | line:%{public}ld => User requested turning off the auto update"
+ "🐞 %{public}s | %{public}s | line:%{public}ld => User requested turning on the auto update"
+ "🐞 %{public}s | %{public}s | line:%{public}ld => finish to refreshBetaUpdates"
+ "🐞 %{public}s | %{public}s | line:%{public}ld => returning %{public}s"
+ "🐞 %{public}s | %{public}s | line:%{public}ld => start to refreshBetaUpdates"
- "Finished to scan for update with results: %s"
- "Intent getting the value of the Automatic Security Response Install: %{bool}d"
- "Intent getting the value of the OS Automatic Download: %{bool}d"
- "Intent setting the value of the Automatic Security Response Install to: %{bool}d"
- "Intent setting the value of the OS Automatic Download to: %{bool}d"
- "Open Apple Beta Software Program or Apple Developer Program settings page"
- "Open Software Update settings page"
- "Perform Software Update now"
- "Perform Software Update tonight"
- "SUSettings Intents got SU Scan Results. Error: %@; results: %@"
- "The Apple Beta Software Program or Apple Developer Program available settings page"
- "🐞 %s | %s | line:%ld => Auto update turned off by user request"
- "🐞 %s | %s | line:%ld => Auto update turned on by user request"
- "🐞 %s | %s | line:%ld => Finished to refreshBetaUpdates"
- "🐞 %s | %s | line:%ld => Perform called with property value: %{bool}d"
- "🐞 %s | %s | line:%ld => Starting to refreshBetaUpdates"
- "🐞 %s | %s | line:%ld => Unable to create SUManagerClient instance"
- "🐞 %s | %s | line:%ld => Unable to create SUSettingsStatefulUIManager"
- "🐞 %s | %s | line:%ld => Unable to init SUManagerClient"
- "🐞 %s | %s | line:%ld => User approved turning off the auto update"
- "🐞 %s | %s | line:%ld => User needs to approved turning off the auto update since there is a scheduled update"
- "🐞 %s | %s | line:%ld => User requested turning off the auto update"
- "🐞 %s | %s | line:%ld => User requested turning on the auto update"
- "🐞 %s | %s | line:%ld => finish to refreshBetaUpdates"
- "🐞 %s | %s | line:%ld => returning %s"
- "🐞 %s | %s | line:%ld => start to refreshBetaUpdates"
```
