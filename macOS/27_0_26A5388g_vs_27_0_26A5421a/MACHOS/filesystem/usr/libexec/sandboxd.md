## sandboxd

> `/usr/libexec/sandboxd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_assocty`
- `__TEXT.__dof_sandboxd`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3051.0.42.0.2
-  __TEXT.__text: 0x33a04
-  __TEXT.__auth_stubs: 0x1600
+3051.0.52.0.0
+  __TEXT.__text: 0x33ee0
+  __TEXT.__auth_stubs: 0x15f0
   __TEXT.__objc_stubs: 0x27a0
   __TEXT.__objc_methlist: 0x10c4
   __TEXT.__const: 0x83b0
-  __TEXT.__cstring: 0x200ab
+  __TEXT.__cstring: 0x200eb
   __TEXT.__oslogstring: 0x2512
   __TEXT.__objc_classname: 0x233
-  __TEXT.__objc_methname: 0x2b70
+  __TEXT.__objc_methname: 0x2b60
   __TEXT.__objc_methtype: 0x67e
   __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__swift5_typeref: 0x18d
+  __TEXT.__swift5_typeref: 0x189
   __TEXT.__constg_swiftt: 0x190
-  __TEXT.__swift5_fieldmd: 0x1cc
+  __TEXT.__swift5_fieldmd: 0x1e4
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_reflstr: 0x1dd
+  __TEXT.__swift5_reflstr: 0x20d
   __TEXT.__swift5_proto: 0x44
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__dof_sandboxd: 0x2f5
-  __TEXT.__unwind_info: 0xa98
+  __TEXT.__unwind_info: 0xaa0
   __TEXT.__eh_frame: 0x370
-  __DATA_CONST.__const: 0x27c0
+  __DATA_CONST.__const: 0x27f0
   __DATA_CONST.__cfstring: 0x84c0
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_intobj: 0x1068
   __DATA_CONST.__objc_arraydata: 0x1388
   __DATA_CONST.__objc_arrayobj: 0xd20
-  __DATA_CONST.__auth_got: 0xb10
+  __DATA_CONST.__auth_got: 0xb08
   __DATA_CONST.__got: 0x328
   __DATA_CONST.__auth_ptr: 0x188
   __DATA.__objc_const: 0x2298

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 991
-  Symbols:   523
-  CStrings:  6025
+  Functions: 992
+  Symbols:   522
+  CStrings:  6026
 
Symbols:
- _$ss22KeyedDecodingContainerV6decode_6forKeyqd__qd__m_xtKSeRd__lF
CStrings:
+ "<plist>\n    <dict>\n\t<key>version</key>\n\t<string>defaultRules-3</string>\n\t<key>protections</key>\n\t<array>\n\t    <!-- Chat Applications -->\n\t    <!-- Discord -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>com.hnc.Discord</string>\n\t\t<key>enforcingPaths</key>\n\t\t<array>\n\t\t    <string>~/Library/Application Support/discord</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>53Q6R32WPB</string>\n\t    </dict>\n\t    <!-- Web Browsers -->\n\t    <!-- Google Chrome -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>com.google.Chrome</string>\n\t\t<key>enforcingPaths</key>\n\t\t<array>\n\t\t    <string>~/Library/Application Support/Google/Chrome</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>EQHXZ8M8AV</string>\n\t\t<key>allowedSigningIds</key>\n\t\t<array>\n\t\t    <string>com.google.Chrome</string>\n\t\t    <string>com.google.Chrome.beta</string>\n\t\t    <string>com.google.Chrome.canary</string>\n\t\t    <string>com.google.Chrome.dev</string>\n\t\t    <string>com.google.Chrome.UpdaterPrivilegedHelper</string>\n\t\t    <string>com.google.GoogleUpdater</string>\n\t\t</array>\n\t\t<key>allowedPlatformSigningIds</key>\n\t\t<array>\n\t\t    <string>com.apple.Safari.BrowserDataImportingService</string>\n\t\t</array>\n\t    </dict>\n\t    <!-- Brave Browser -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>com.brave.Browser</string>\n\t\t<key>enforcingPaths</key>\n\t\t<array>\n\t\t    <string>~/Library/Application Support/BraveSoftware/Brave-Browser</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>KL8N8XSYF4</string>\n\t\t<key>allowedSigningIds</key>\n\t\t<array>\n\t\t    <string>com.brave.Browser</string>\n\t\t    <string>com.brave.Browser.beta</string>\n\t\t    <string>com.brave.Browser.nightly</string>\n\t\t    <string>com.brave.Browser.dev</string>\n\t\t    <string>com.brave.Browser.UpdaterPrivilegedHelper</string>\n\t\t    <string>com.brave.BraveUpdater</string>\n\t\t</array>\n\t    </dict>\n\t    <!-- Microsoft Edge -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>com.microsoft.edgemac</string>\n\t\t<key>enforcingPaths</key>\n\t\t<array>\n\t\t    <string>~/Library/Application Support/Microsoft Edge</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>UBF8T346G9</string>\n\t\t<key>allowedSigningIds</key>\n\t\t<array>\n\t\t    <string>com.microsoft.edgemac</string>\n\t\t    <string>com.microsoft.edgemac.Beta</string>\n\t\t    <string>com.microsoft.edgemac.Canary</string>\n\t\t    <string>com.microsoft.edgemac.Dev</string>\n\t\t    <string>com.microsoft.edgemac.local</string>\n\t\t    <string>com.microsoft.EdgeUpdater</string>\n\t\t    <string>com.microsoft.EdgeUpdater.helper</string>\n\t\t</array>\n\t    </dict>\n\t    <!-- Firefox -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>org.mozilla.firefox</string>\n\t\t<key>enforcingPaths</key>\n\t\t<array>\n\t\t    <string>~/Library/Application Support/Firefox</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>43AQ936H96</string>\n\t\t<key>allowedPlatformSigningIds</key>\n\t\t<array>\n\t\t    <string>com.apple.Safari.BrowserDataImportingService</string>\n\t\t</array>\n\t    </dict>\n\t    <!-- Crypto Wallets -->\n\t    <!-- Ledger Live -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>com.ledger.live</string>\n\t\t<key>enforcingPaths</key>\n\t\t<array>\n\t\t    <string>~/Library/Application Support/Ledger Live</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>X6LFS5BQKN</string>\n\t    </dict>\n\t    <!-- Exodus -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>com.electron.exodus</string>\n\t\t<key>enforcingPaths</key>\n\t\t<array>\n\t\t    <string>~/Library/Application Support/Exodus</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>VK5Q293EVL</string>\n\t    </dict>\n\t    <!-- Wasabi -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>zksnacks.wasabiwallet</string>\n\t\t<key>enforcingPaths</key>\n\t\t<array>\n\t\t    <string>~/.walletwasabi</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>L233B2JQ68</string>\n\t    </dict>\n\t</array>\n\t<key>exclusions</key>\n\t<array>\n\t    <string>~/Library/Application Support/BraveSoftware/Brave-Browser/NativeMessagingHosts</string>\n\t    <string>~/Library/Application Support/Google/Chrome/NativeMessagingHosts</string>\n\t    <string>~/Library/Application Support/Microsoft Edge/NativeMessagingHosts</string>\n\t    <string>~/Library/Application Support/Mozilla/NativeMessagingHosts</string>\n\t    <!-- For Progressive Web Apps -->\n\t    <string>~/Library/Application Support/Google/Chrome/ChromeFeatureState</string>\n\t    <string>~/Library/Application Support/Google/Chrome/Crashpad</string>\n\t</array>\n    </dict>\n</plist>"
+ "Aug 11 2026"
+ "enforcingPaths"
+ "nonenforcingPaths"
- "<plist>\n    <dict>\n\t<key>version</key>\n\t<string>defaultRules-2</string>\n\t<key>protections</key>\n\t<array>\n\t    <!-- Chat Applications -->\n\t    <!-- Discord -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>com.hnc.Discord</string>\n\t\t<key>paths</key>\n\t\t<array>\n\t\t    <string>~/Library/Application Support/discord</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>53Q6R32WPB</string>\n\t\t<key>enforce</key>\n\t\t<true/>\n\t    </dict>\n\t    <!-- Web Browsers -->\n\t    <!-- Google Chrome -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>com.google.Chrome</string>\n\t\t<key>paths</key>\n\t\t<array>\n\t\t    <string>~/Library/Application Support/Google/Chrome</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>EQHXZ8M8AV</string>\n\t\t<key>allowedSigningIds</key>\n\t\t<array>\n\t\t    <string>com.google.Chrome</string>\n\t\t    <string>com.google.Chrome.beta</string>\n\t\t    <string>com.google.Chrome.canary</string>\n\t\t    <string>com.google.Chrome.dev</string>\n\t\t    <string>com.google.Chrome.UpdaterPrivilegedHelper</string>\n\t\t    <string>com.google.GoogleUpdater</string>\n\t\t</array>\n\t\t<key>allowedPlatformSigningIds</key>\n\t\t<array>\n\t\t    <string>com.apple.Safari.BrowserDataImportingService</string>\n\t\t</array>\n\t\t<key>enforce</key>\n\t\t<true/>\n\t    </dict>\n\t    <!-- Brave Browser -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>com.brave.Browser</string>\n\t\t<key>paths</key>\n\t\t<array>\n\t\t    <string>~/Library/Application Support/BraveSoftware/Brave-Browser</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>KL8N8XSYF4</string>\n\t\t<key>allowedSigningIds</key>\n\t\t<array>\n\t\t    <string>com.brave.Browser</string>\n\t\t    <string>com.brave.Browser.beta</string>\n\t\t    <string>com.brave.Browser.nightly</string>\n\t\t    <string>com.brave.Browser.dev</string>\n\t\t    <string>com.brave.Browser.UpdaterPrivilegedHelper</string>\n\t\t    <string>com.brave.BraveUpdater</string>\n\t\t</array>\n\t\t<key>enforce</key>\n\t\t<true/>\n\t    </dict>\n\t    <!-- Microsoft Edge -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>com.microsoft.edgemac</string>\n\t\t<key>paths</key>\n\t\t<array>\n\t\t    <string>~/Library/Application Support/Microsoft Edge</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>UBF8T346G9</string>\n\t\t<key>allowedSigningIds</key>\n\t\t<array>\n\t\t    <string>com.microsoft.edgemac</string>\n\t\t    <string>com.microsoft.edgemac.Beta</string>\n\t\t    <string>com.microsoft.edgemac.Canary</string>\n\t\t    <string>com.microsoft.edgemac.Dev</string>\n\t\t    <string>com.microsoft.edgemac.local</string>\n\t\t    <string>com.microsoft.EdgeUpdater</string>\n\t\t    <string>com.microsoft.EdgeUpdater.helper</string>\n\t\t</array>\n\t\t<key>enforce</key>\n\t\t<true/>\n\t    </dict>\n\t    <!-- Firefox -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>org.mozilla.firefox</string>\n\t\t<key>paths</key>\n\t\t<array>\n\t\t    <string>~/Library/Application Support/Firefox</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>43AQ936H96</string>\n\t\t<key>allowedPlatformSigningIds</key>\n\t\t<array>\n\t\t    <string>com.apple.Safari.BrowserDataImportingService</string>\n\t\t</array>\n\t\t<key>enforce</key>\n\t\t<true/>\n\t    </dict>\n\t    <!-- Crypto Wallets -->\n\t    <!-- Ledger Live -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>com.ledger.live</string>\n\t\t<key>paths</key>\n\t\t<array>\n\t\t    <string>~/Library/Application Support/Ledger Live</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>X6LFS5BQKN</string>\n\t\t<key>enforce</key>\n\t\t<true/>\n\t    </dict>\n\t    <!-- Exodus -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>com.electron.exodus</string>\n\t\t<key>paths</key>\n\t\t<array>\n\t\t    <string>~/Library/Application Support/Exodus</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>VK5Q293EVL</string>\n\t\t<key>enforce</key>\n\t\t<true/>\n\t    </dict>\n\t    <!-- Wasabi -->\n\t    <dict>\n\t\t<key>attribution</key>\n\t\t<string>zksnacks.wasabiwallet</string>\n\t\t<key>paths</key>\n\t\t<array>\n\t\t    <string>~/.walletwasabi</string>\n\t\t</array>\n\t\t<key>allowedTeamId</key>\n\t\t<string>L233B2JQ68</string>\n\t\t<key>enforce</key>\n\t\t<true/>\n\t    </dict>\n\t</array>\n\t<key>exclusions</key>\n\t<array>\n\t    <string>~/Library/Application Support/BraveSoftware/Brave-Browser/NativeMessagingHosts</string>\n\t    <string>~/Library/Application Support/Google/Chrome/NativeMessagingHosts</string>\n\t    <string>~/Library/Application Support/Microsoft Edge/NativeMessagingHosts</string>\n\t    <string>~/Library/Application Support/Mozilla/NativeMessagingHosts</string>\n\t</array>\n    </dict>\n</plist>"
- "Jul 14 2026"
- "TB,N,R,Venforce"
```
