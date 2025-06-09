## AKAppSSOExtension

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension`

```diff

-493.463.1.0.0
-  __TEXT.__text: 0x6ff0
-  __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_stubs: 0x1080
-  __TEXT.__objc_methlist: 0x4fc
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x3445
+512.1.3.0.0
+  __TEXT.__text: 0x7450
+  __TEXT.__auth_stubs: 0x400
+  __TEXT.__objc_stubs: 0x11e0
+  __TEXT.__objc_methlist: 0x524
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x40ad
   __TEXT.__objc_classname: 0xc9
-  __TEXT.__objc_methname: 0x1403
+  __TEXT.__objc_methname: 0x1501
   __TEXT.__objc_methtype: 0x2b3
-  __TEXT.__gcc_except_tab: 0x1f4
-  __TEXT.__oslogstring: 0x7e2
-  __TEXT.__unwind_info: 0x1a8
-  __DATA_CONST.__auth_got: 0x200
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x348
-  __DATA_CONST.__cfstring: 0x2060
+  __TEXT.__gcc_except_tab: 0x214
+  __TEXT.__oslogstring: 0x827
+  __TEXT.__unwind_info: 0x1b8
+  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__const: 0x3a0
+  __DATA_CONST.__cfstring: 0x21c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x168
-  __DATA_CONST.__objc_arraydata: 0xe28
-  __DATA_CONST.__objc_dictobj: 0xaf0
+  __DATA_CONST.__objc_arraydata: 0xe70
+  __DATA_CONST.__objc_dictobj: 0xb18
   __DATA_CONST.__objc_arrayobj: 0x240
   __DATA.__objc_const: 0x748
-  __DATA.__objc_selrefs: 0x660
+  __DATA.__objc_selrefs: 0x6b8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x120
+  __DATA.__data: 0x130
   __DATA.__bss: 0x58
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/URLFormatting.framework/URLFormatting
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 76C32106-A97A-3D8F-8FCE-24EAB17ACF29
-  Functions: 120
-  Symbols:   178
-  CStrings:  816
+  UUID: 4C9FF374-E722-34C6-A3C2-DE9EAB99DEB3
+  Functions: 125
+  Symbols:   184
+  CStrings:  851
 
Symbols:
+ _AKTestBAADeviceTokenBase64
+ _AKTestBAADeviceTokenKey
+ _AKTestBAADeviceTokenValue
+ _OBJC_CLASS_$_AKAlertHandler
+ _objc_retain_x27
+ _objc_retain_x28
CStrings:
+ "6288675309"
+ "<?xml version=\"1.0\" encoding=\"UTF-8\"?>        <!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">        <plist version=\"1.0\">        <dict>            <key>env</key>            <dict>                <key>apsEnv</key>                <string>production</string>                <key>idmsEnv</key>                <string>IdMS</string>            </dict>            <key>urls</key>            <dict>                <key>gsService</key>                <dict>                    <key>url</key>                    <string>https://gsa.apple.com/grandslam/GsService2</string>                </dict>                <key>fetchAuthorizedApps</key>                <dict>                    <key>url</key>                    <string>https://gsa.apple.com/grandslam/GsService2/fetchAuthorizedApps</string>                </dict>                <key>fetchUserInfo</key>                <dict>                    <key>url</key>                    <string>https://gsa.apple.com/grandslam/GsService2/fetchUserInfo</string>                </dict>                <key>federatedIntro</key>                <dict>                    <key>url</key>                    <string>%@</string>                </dict>                <key>repair</key>                <dict>                    <key>url</key>                    <string>https://gsa.apple.com/grandslam/GsService2/repair</string>                </dict>                <key>securityUpgrade</key>                <dict>                    <key>url</key>                    <string>https://gsa.apple.com/appleid/account/security/upgrade</string>                </dict>                <key>createAccount</key>                <dict>                    <key>url</key>                    <string>https://gsa.apple.com/appleid/account</string>                </dict>                <key>createChildAccount</key>                <dict>                    <key>url</key>                    <string>https://gsa.apple.com/appleid/account/child</string>                </dict>                <key>createTeenAccount</key>                <dict>                    <key>url</key>                    <string>https://gsa.apple.com/appleid/account/teen</string>                </dict>                <key>signInAlert</key>                <dict>                    <key>url</key>                    <string>https://gsa.apple.com/appleid/settings/account/manage/security/key/notify/auth</string>                </dict>                <key>iForgot</key>                <dict>                    <key>url</key>                    <string>https://gsa.apple.com/iforgot</string>                </dict>                <key>fetchAuthMode</key>                <dict>                    <key>url</key>                    <string>https://gsa.apple.com/grandslam/GsService2/fetchAuthMode</string>                </dict>                <key>passwordChange</key>                <dict>                    <key>url</key>                    <string>https://gsa.apple.com/appleid/account/manage/security/password</string>                </dict>                <key>secondaryAuth</key>                <dict>                    <key>url</key>                    <string>https://gsa.apple.com/appleid/settings/authenticate</string>                </dict>                <key>device_list_self</key>                <dict>                    <key>url</key>                    <string>https://gsa.apple.com/device_list_self</string>                </dict>                <key>collabAccountUpgrade</key>                <dict>                    <key>url</key>                    <string>https://gsa.apple.com/collabAccountUpgrade</string>                </dict>            </dict>        </dict>    </plist>"
+ "Finished showing validator error with result: %d and alert error: %@"
+ "URL"
+ "X-Apple-HB-Token"
+ "X-Apple-I-CK"
+ "X-Apple-I-PRK"
+ "Y29tLmFwcGxlLmdzLmlkbXMuaGI6QUFBQUJMd0lBQUFBQUdlU3FEVVJDbWR6TG1sa2JYTXVhR0tPQkFBQUFDaTlBQVgvcVlkVDZXZENoZGg5V0ZKblp3S1JFZzVXZlIyV2NIRVpmS3lXMmloZ1dTa01LTmN6QUhvV254cnl5ZCt2VTdqcDByQU9IVTZGR01WMk1hc1ByTjdlM2xJVTVzc0VwbDdsZjlPc0JFZDIwMVNxZTN3amxuZVRUVU04MmZXQ0V5eW41eEtwMWprbXZyZ3dpTEx6L3Y2YWVCdFNlYk9wN3duUGl0T3FaSy9mZnUrenlDbnFCQnVqc2NJWTdrTExheVorSnQwPTozMTUzNjAwMDoxNzM3NjY0NTY1NjQy"
+ "_getIconTypeIDForHostName:"
+ "_sharedKeyInfo"
+ "allHeaderFields"
+ "code"
+ "com.apple.application-icon.icloud"
+ "dGVzdEJBQURldmljZVRva2VuOjYyODg2NzUzMDk="
+ "data"
+ "isSecurePakeEnabled"
+ "isURLFromAllowListDomainsForSharingKey:"
+ "mid"
+ "set_iconTypeID:"
+ "sharing_key"
+ "showAlertForError:withCompletion:"
+ "successfulChildAccountCreationResponse"
+ "successfulTeenAccountCreationResponse"
+ "testBAADeviceToken:6288675309"
+ "v20@?0B8@\"NSError\"12"
- "<?xml version=\"1.0\" encoding=\"UTF-8\"?>         <!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">         <plist version=\"1.0\">         <dict>             <key>env</key>             <dict>                 <key>apsEnv</key>                 <string>production</string>                 <key>idmsEnv</key>                 <string>IdMS</string>             </dict>             <key>urls</key>             <dict>                 <key>gsService</key>                 <dict>                     <key>url</key>                     <string>https://gsa.apple.com/grandslam/GsService2</string>                 </dict>                 <key>fetchAuthorizedApps</key>                 <dict>                     <key>url</key>                     <string>https://gsa.apple.com/grandslam/GsService2/fetchAuthorizedApps</string>                 </dict>                 <key>fetchUserInfo</key>                 <dict>                     <key>url</key>                     <string>https://gsa.apple.com/grandslam/GsService2/fetchUserInfo</string>                 </dict>             </dict>         </dict>     </plist>"

```
