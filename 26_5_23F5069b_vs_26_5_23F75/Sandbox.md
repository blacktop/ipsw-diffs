## Sandbox Profiles

### Collection

#### Changed (27)

##### IMTranscoderAgent

```diff

 )
 (deny mach-lookup
 	(require-any
-		(xpc-service-name "com.apple.CoreGraphics.CGPDFService")
 		(xpc-service-name "com.apple.WebKit.*")
+		(xpc-service-name "com.apple.CoreGraphics.CGPDFService")
 	)
 )
 
```

##### MobileBackup

```diff

 
 (deny file-write-setugid
 	(require-any
-		(require-not (vnode-type DIRECTORY))
 		(subpath "/private/var/run/mobile_image_mounter")
+		(require-not (vnode-type DIRECTORY))
 	)
 )
 
 (deny file-write-unlink
 	(require-any
+		(subpath "/private/var/run/mobile_image_mounter")
 		(literal "/private")
 		(literal "/private/var")
 		(literal "/private/var/run")
-		(subpath "/private/var/run/mobile_image_mounter")
 	)
 )
 
```

##### MobileSlideShow

```diff

 	)
 )
 
-(allow file-write-acl
+(allow file-write-create
 	(require-all
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 		(subpath "${HOME}/Library/AddressBook/Delegates")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
 	)
 )
-(allow file-write-acl
-	(require-all
-		(subpath "/private/var")
-		(subpath "${HOME}")
-		(require-any
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/DiagnosticLogs/Camera-latest.log")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/SpringBoard/.*(Lock|Home).+")
-		)
-	)
-)
-(allow file-write-acl
-	(require-all
-		(subpath "${HOME}/Library/Mobile Documents")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-)
-(allow file-write-acl
-	(require-all
-		(extension "com.apple.classkit.read-write")
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit")
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/ClassKit(/|$)")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-			)
-		)
-	)
-)
-(allow file-write-acl
-	(require-all
-		(extension "com.apple.fileprovider.read-write")
-		(require-any
-			(require-any
-				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd")
-				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
-				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
-			)
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
-				(subpath "${FRONT_USER_HOME}")
-			)
-		)
-	)
-)
-(allow file-write-acl
-	(require-all
-		(process-attribute is-apple-signed-executable)
-		(subpath "${HOME}/Library/Caches/com.apple.keyboards")
-	)
-)
-(allow file-write-acl
-	(require-all
-		(subpath "/private/var")
-		(subpath "${HOME}")
-		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-					(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-				)
-			)
-			(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-		)
-	)
-)
-(allow file-write-acl
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-)
-(allow file-write-acl
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-)
-(allow file-write-acl
-	(require-all
-		(vnode-type REGULAR-FILE)
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(subpath "${HOME}/Library/AddressBook")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
-	)
-)
-(allow file-write-acl
+(allow file-write-create
 	(require-all
 		(signing-identifier "com.apple.camera.lockscreen")
 		(extension "com.apple.sandbox.container")

 		)
 	)
 )
-(allow file-write-acl
+(allow file-write-create
+	(require-all
+		(subpath "${HOME}/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-create
 	(require-all
 		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-		(subpath "${FRONT_USER_HOME}")
+		(subpath "${HOME}")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-			(extension "com.apple.librarian.ubiquity-container")
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/DiagnosticLogs/Camera-latest.log")
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/SpringBoard/.*(Lock|Home).+")
 		)
 	)
 )
-(allow file-write-acl
+(allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(extension "com.apple.fileprovider.read-write")
 		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.camera")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.mobileslideshow")
+			(require-any
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+			)
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
+				(subpath "${FRONT_USER_HOME}")
+			)
 		)
 	)
 )
-(allow file-write-acl
+(allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE SYMLINK)
-		(require-any
-			(subpath "/private/var/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-		)
-		(extension "com.apple.revisiond.staging")
+		(vnode-type REGULAR-FILE)
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(subpath "${HOME}/Library/AddressBook")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
 	)
 )
-(allow file-write-acl
+(allow file-write-create
 	(require-all
-		(extension "com.apple.sandbox.application-group")
+		(subpath "/private/var")
+		(subpath "${HOME}")
+		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
 			(require-all
-				(subpath "/private/var")
+				(vnode-type DIRECTORY)
 				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						)
-					)
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+					(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
 				)
 			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
-			)
+			(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
 		)
 	)
 )
-(allow file-write-acl
+(allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
-		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.photos.peopleImageCache")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 	)
 )
-(allow file-write-acl
-	(require-any
-		(literal "${HOME}/Library/SpringBoard")
-		(subpath "${HOME}/Library/Caches/Snapshots/com.apple.camera")
-		(require-any
-			(subpath "${HOME}/Library/Siri")
-			(literal "${HOME}/Library/Logs/MobileSlideShow.log")
-			(literal "${HOME}/Library/Logs/awd/awd-Camera.log")
-			(literal "${HOME}/Library/Logs/awd/awd-MobileSlideShow.log")
-			(literal "${HOME}/Library/Logs/awd/awdComponent0x19.log")
-			(subpath "${HOME}/Library/Application Support/MobileSlideShow")
-			(subpath "${HOME}/Library/Application Support/iLifePageLayout")
-			(subpath "${HOME}/Library/Caches/com.apple.legacycamera")
-			(subpath "${HOME}/Library/Caches/com.apple.springboard.sharedimagecache/Wallpaper")
-		)
-		(subpath "${HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CloudPhotoLibrary.aslgroup")
-		(subpath "${HOME}/Library/SMS")
-		(subpath "${HOME}/Library/Logs/CrashReporter/DiagnosticLogs/Photos")
-		(subpath "${HOME}/Library/Cookies")
-		(literal "${HOME}/Library/Caches/com.apple.pep.configuration.plist")
-		(subpath "${HOME}/Library/Caches/com.apple.photos.peopleImageCache")
-		(subpath "${HOME}/Media/Debug")
-		(require-any
-			(subpath "${HOME}/Media/Safari")
-			(subpath "${HOME}/Documents/com.apple.camera.settings")
-			(subpath "${HOME}/Documents/com.apple.mobileslideshow.settings")
-			(subpath "${HOME}/Library/WebKit")
-			(literal "${HOME}/Library/Caches/Snapshots/com.apple.camera-*")
-			(literal "${HOME}/Library/Caches/Snapshots/com.apple.mobileslideshow-*")
-			(subpath "${HOME}/Library/Caches/Snapshots/com.apple.mobileslideshow")
-			(subpath "${HOME}/Library/Saved Application State/com.apple.camera\\.savedState")
-			(subpath "${HOME}/Library/Saved Application State/com.apple.mobileslideshow\\.savedState")
-		)
-		(subpath "${HOME}/Media/MediaAnalysis")
-		(subpath "/private/var/tmp")
-		(subpath "${HOME}/Media/PhotoData")
-		(subpath "${HOME}/Media/Memories")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.camera")
-			(subpath "${HOME}/Library/Caches/com.apple.mobileslideshow")
-		)
-		(literal "${HOME}/Library/Preferences/com.apple.dataaccess.launchd")
+(allow file-write-create
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-create
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+		(subpath "${FRONT_USER_HOME}")
 		(require-any
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.camera")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileslideshow")
+			(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+			(extension "com.apple.librarian.ubiquity-container")
 		)
-		(subpath "${HOME}/Media/DCIM")
-		(subpath "${HOME}/Media/Photos")
-		(subpath "${PROCESS_TEMP_DIR}")
-		(subpath "${HOME}/Library/WebClips")
 	)
 )
-(deny file-write-acl
+(allow file-write-create
 	(require-all
 		(extension "com.apple.sandbox.application-group")
 		(require-any

 		)
 	)
 )
-(deny file-write-acl
+(allow file-write-create
 	(require-all
-		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-only"))
-		(require-not (extension "com.apple.app-sandbox.read"))
-		(require-not (extension "com.apple.app-sandbox.read-write"))
-		(require-not (extension "com.apple.sandbox.executable"))
-		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-write"))
+		(vnode-type DIRECTORY REGULAR-FILE)
 		(require-any
-			(subpath "${ANY_USER_HOME}/Containers")
-			(subpath "/private/var/containers")
+			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.camera")
+			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.mobileslideshow")
 		)
 	)
 )
-(deny file-write-acl
+(allow file-write-create
 	(require-all
-		(signing-identifier "com.apple.camera.lockscreen")
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/SyncedPreferences")
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
-									(require-all
-										(signing-identifier "com.apple.camera.lockscreen")
-										(subpath "/private/var")
-										(extension "com.apple.sandbox.container")
-										(require-any
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-													(require-all
-														(require-any
-															(subpath "${FRONT_USER_HOME}")
-															(subpath "${HOME}")
-														)
-														(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-													)
-												)
-											)
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
-							(require-all
-								(signing-identifier "com.apple.camera.lockscreen")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-											)
-										)
-									)
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.camera.lockscreen")
-						(subpath "/private/var")
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-									)
-								)
-							)
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(deny file-write-acl
-	(require-any
-		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-		(literal "${ANY_USER_HOME}/Library/Preferences/com.apple.mobileipod.plist")
-		(literal "${HOME}/Library/Preferences/com.apple.springboard.plist*")
-		(literal "${HOME}/Library/Caches/DateFormats.plist")
-	)
-)
-
-(allow file-write-create
-	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(subpath "${HOME}/Library/AddressBook/Delegates")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
-	)
-)
-(allow file-write-create
-	(require-all
-		(signing-identifier "com.apple.camera.lockscreen")
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/SyncedPreferences")
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
-									(require-all
-										(signing-identifier "com.apple.camera.lockscreen")
-										(subpath "/private/var")
-										(extension "com.apple.sandbox.container")
-										(require-any
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-													(require-all
-														(require-any
-															(subpath "${FRONT_USER_HOME}")
-															(subpath "${HOME}")
-														)
-														(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-													)
-												)
-											)
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
-							(require-all
-								(signing-identifier "com.apple.camera.lockscreen")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-											)
-										)
-									)
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.camera.lockscreen")
-						(subpath "/private/var")
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-									)
-								)
-							)
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-write-create
-	(require-all
-		(subpath "${HOME}/Library/Mobile Documents")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-)
-(allow file-write-create
-	(require-all
-		(subpath "/private/var")
-		(subpath "${HOME}")
-		(require-any
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/DiagnosticLogs/Camera-latest.log")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/SpringBoard/.*(Lock|Home).+")
-		)
-	)
-)
-(allow file-write-create
-	(require-all
-		(extension "com.apple.fileprovider.read-write")
-		(require-any
-			(require-any
-				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd")
-				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
-				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
-			)
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
-				(subpath "${FRONT_USER_HOME}")
-			)
-		)
-	)
-)
-(allow file-write-create
-	(require-all
-		(vnode-type REGULAR-FILE)
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(subpath "${HOME}/Library/AddressBook")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
-	)
-)
-(allow file-write-create
-	(require-all
-		(subpath "/private/var")
-		(subpath "${HOME}")
-		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-					(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-				)
-			)
-			(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-		)
-	)
-)
-(allow file-write-create
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-)
-(allow file-write-create
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-)
-(allow file-write-create
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-		(subpath "${FRONT_USER_HOME}")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-			(extension "com.apple.librarian.ubiquity-container")
-		)
-	)
-)
-(allow file-write-create
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						)
-					)
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-				)
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
-			)
-		)
-	)
-)
-(allow file-write-create
-	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.camera")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.mobileslideshow")
-		)
-	)
-)
-(allow file-write-create
-	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE SYMLINK)
+		(vnode-type DIRECTORY REGULAR-FILE SYMLINK)
 		(require-any
 			(subpath "/private/var/.DocumentRevisions-V100/staging")
 			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")

 )
 (deny file-write-create
 	(require-any
-		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 		(literal "${HOME}/Library/Logs/CrashReporter/CFNetwork_*")
 		(require-any
 			(literal "${HOME}/Library/Preferences/com.apple.UIKit.plist*")

 		(literal "${ANY_USER_HOME}/Library/Preferences/com.apple.mobileipod.plist")
 		(literal "${HOME}/Library/Preferences/com.apple.springboard.plist*")
 		(literal "${HOME}/Library/Caches/DateFormats.plist")
+		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 	)
 )
 

 	)
 )
 
-(deny file-write-setugid)
-
-(allow file-write-unlink
-	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-)
-(allow file-write-unlink
+(allow file-write-owner
 	(require-all
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 		(subpath "${HOME}/Library/AddressBook/Delegates")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
 	)
 )
-(allow file-write-unlink
+(allow file-write-owner
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(subpath "${HOME}/Library/AddressBook")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(subpath "/private/var")
+		(subpath "${HOME}")
+		(require-any
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/DiagnosticLogs/Camera-latest.log")
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/SpringBoard/.*(Lock|Home).+")
+		)
 	)
 )
-(allow file-write-unlink
+(allow file-write-owner
 	(require-all
 		(subpath "${HOME}/Library/Mobile Documents")
 		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 	)
 )
-(allow file-write-unlink
+(allow file-write-owner
 	(require-all
 		(extension "com.apple.classkit.read-write")
 		(require-any

 		)
 	)
 )
-(allow file-write-unlink
+(allow file-write-owner
 	(require-all
 		(extension "com.apple.fileprovider.read-write")
 		(require-any

 		)
 	)
 )
-(allow file-write-unlink
+(allow file-write-owner
 	(require-all
-		(extension "com.apple.sandbox.application-group")
+		(process-attribute is-apple-signed-executable)
+		(subpath "${HOME}/Library/Caches/com.apple.keyboards")
+	)
+)
+(allow file-write-owner
+	(require-all
+		(subpath "/private/var")
+		(subpath "${HOME}")
+		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
 			(require-all
-				(subpath "/private/var")
+				(vnode-type DIRECTORY)
 				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						)
-					)
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+					(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
 				)
 			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
-			)
+			(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
 		)
 	)
 )
-(allow file-write-unlink
+(allow file-write-owner
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-owner
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-owner
+	(require-all
+		(vnode-type REGULAR-FILE)
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(subpath "${HOME}/Library/AddressBook")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
+	)
+)
+(allow file-write-owner
 	(require-all
+		(signing-identifier "com.apple.camera.lockscreen")
 		(extension "com.apple.sandbox.container")
 		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/SyncedPreferences")
 			(require-all
 				(subpath "/private/var")
 				(require-any
 					(require-all
 						(subpath "/private/var/PersonaVolumes")
 						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$")
-								(signing-identifier "com.apple.camera.lockscreen")
-							)
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
 							(require-all
 								(require-any
 									(subpath "${FRONT_USER_HOME}")
 									(subpath "${HOME}")
 								)
 								(require-any
-									(require-all
-										(regex #"((((((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)")
-										(signing-identifier "com.apple.camera.lockscreen")
-									)
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
 									(require-all
 										(signing-identifier "com.apple.camera.lockscreen")
+										(subpath "/private/var")
+										(extension "com.apple.sandbox.container")
 										(require-any
 											(require-all
 												(subpath "/private/var/PersonaVolumes")
 												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
 													(require-all
 														(require-any
 															(subpath "${FRONT_USER_HOME}")
 															(subpath "${HOME}")
 														)
-														(require-any
-															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
-															(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-														)
+														(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
 													)
 												)
 											)

 													(subpath "${FRONT_USER_HOME}")
 													(subpath "${HOME}")
 												)
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
-													(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-												)
+												(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
 											)
-											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
 										)
 									)
 								)

 							(subpath "${HOME}")
 						)
 						(require-any
-							(require-all
-								(regex #"((((((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)")
-								(signing-identifier "com.apple.camera.lockscreen")
-							)
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
 							(require-all
 								(signing-identifier "com.apple.camera.lockscreen")
+								(subpath "/private/var")
+								(extension "com.apple.sandbox.container")
 								(require-any
 									(require-all
 										(subpath "/private/var/PersonaVolumes")
 										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
 											(require-all
 												(require-any
 													(subpath "${FRONT_USER_HOME}")
 													(subpath "${HOME}")
 												)
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
-													(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-												)
+												(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
 											)
 										)
 									)

 											(subpath "${FRONT_USER_HOME}")
 											(subpath "${HOME}")
 										)
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
-											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-										)
+										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
 									)
-									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
 								)
 							)
 						)
 					)
 					(require-all
 						(signing-identifier "com.apple.camera.lockscreen")
+						(subpath "/private/var")
+						(extension "com.apple.sandbox.container")
 						(require-any
 							(require-all
 								(subpath "/private/var/PersonaVolumes")
 								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
 									(require-all
 										(require-any
 											(subpath "${FRONT_USER_HOME}")
 											(subpath "${HOME}")
 										)
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
-											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-										)
+										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
 									)
 								)
 							)

 									(subpath "${FRONT_USER_HOME}")
 									(subpath "${HOME}")
 								)
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
-									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-								)
+								(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
 							)
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
 						)
 					)
 				)
 			)
+		)
+	)
+)
+(allow file-write-owner
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+		(subpath "${FRONT_USER_HOME}")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+			(extension "com.apple.librarian.ubiquity-container")
+		)
+	)
+)
+(allow file-write-owner
+	(require-all
+		(vnode-type DIRECTORY REGULAR-FILE)
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.camera")
+			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.mobileslideshow")
+		)
+	)
+)
+(allow file-write-owner
+	(require-all
+		(vnode-type DIRECTORY REGULAR-FILE SYMLINK)
+		(require-any
+			(subpath "/private/var/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+		)
+		(extension "com.apple.revisiond.staging")
+	)
+)
+(allow file-write-owner
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
 			(require-all
-				(signing-identifier "com.apple.camera.lockscreen")
+				(subpath "/private/var")
 				(require-any
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
 					(require-all
-						(subpath "/private/var")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
 						(require-any
 							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
 					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 				)
 			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
 		)
 	)
 )
-(allow file-write-unlink
+(allow file-write-owner
 	(require-all
 		(vnode-type DIRECTORY REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.photos.peopleImageCache")
 	)
 )
-(allow file-write-unlink
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE SYMLINK)
+(allow file-write-owner
+	(require-any
+		(literal "${HOME}/Library/SpringBoard")
+		(subpath "${HOME}/Library/Caches/Snapshots/com.apple.camera")
 		(require-any
-			(subpath "/private/var/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+			(subpath "${HOME}/Library/Siri")
+			(literal "${HOME}/Library/Logs/MobileSlideShow.log")
+			(literal "${HOME}/Library/Logs/awd/awd-Camera.log")
+			(literal "${HOME}/Library/Logs/awd/awd-MobileSlideShow.log")
+			(literal "${HOME}/Library/Logs/awd/awdComponent0x19.log")
+			(subpath "${HOME}/Library/Application Support/MobileSlideShow")
+			(subpath "${HOME}/Library/Application Support/iLifePageLayout")
+			(subpath "${HOME}/Library/Caches/com.apple.legacycamera")
+			(subpath "${HOME}/Library/Caches/com.apple.springboard.sharedimagecache/Wallpaper")
 		)
-		(extension "com.apple.revisiond.staging")
+		(subpath "${HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CloudPhotoLibrary.aslgroup")
+		(subpath "${HOME}/Library/SMS")
+		(subpath "${HOME}/Library/Logs/CrashReporter/DiagnosticLogs/Photos")
+		(subpath "${HOME}/Library/Cookies")
+		(literal "${HOME}/Library/Caches/com.apple.pep.configuration.plist")
+		(subpath "${HOME}/Library/Caches/com.apple.photos.peopleImageCache")
+		(subpath "${HOME}/Media/Debug")
+		(require-any
+			(subpath "${HOME}/Media/Safari")
+			(subpath "${HOME}/Documents/com.apple.camera.settings")
+			(subpath "${HOME}/Documents/com.apple.mobileslideshow.settings")
+			(subpath "${HOME}/Library/WebKit")
+			(literal "${HOME}/Library/Caches/Snapshots/com.apple.camera-*")
+			(literal "${HOME}/Library/Caches/Snapshots/com.apple.mobileslideshow-*")
+			(subpath "${HOME}/Library/Caches/Snapshots/com.apple.mobileslideshow")
+			(subpath "${HOME}/Library/Saved Application State/com.apple.camera\\.savedState")
+			(subpath "${HOME}/Library/Saved Application State/com.apple.mobileslideshow\\.savedState")
+		)
+		(subpath "${HOME}/Media/MediaAnalysis")
+		(subpath "/private/var/tmp")
+		(subpath "${HOME}/Media/PhotoData")
+		(subpath "${HOME}/Media/Memories")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.camera")
+			(subpath "${HOME}/Library/Caches/com.apple.mobileslideshow")
+		)
+		(literal "${HOME}/Library/Preferences/com.apple.dataaccess.launchd")
+		(require-any
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.camera")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileslideshow")
+		)
+		(subpath "${HOME}/Media/DCIM")
+		(subpath "${HOME}/Media/Photos")
+		(subpath "${PROCESS_TEMP_DIR}")
+		(subpath "${HOME}/Library/WebClips")
 	)
 )
-(allow file-write-unlink
+(deny file-write-owner
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(extension "com.apple.sandbox.application-group")
 		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.camera")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.mobileslideshow")
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
 		)
 	)
 )
-(allow file-write-unlink
+(deny file-write-owner
 	(require-all
-		(process-attribute is-apple-signed-executable)
-		(subpath "${HOME}/Library/Caches/com.apple.keyboards")
+		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-only"))
+		(require-not (extension "com.apple.app-sandbox.read"))
+		(require-not (extension "com.apple.app-sandbox.read-write"))
+		(require-not (extension "com.apple.sandbox.executable"))
+		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-write"))
+		(require-any
+			(subpath "${ANY_USER_HOME}/Containers")
+			(subpath "/private/var/containers")
+		)
 	)
 )
-(allow file-write-unlink
+(deny file-write-owner
 	(require-all
 		(signing-identifier "com.apple.camera.lockscreen")
 		(extension "com.apple.sandbox.container")

 		)
 	)
 )
+(deny file-write-owner
+	(require-any
+		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
+		(literal "${ANY_USER_HOME}/Library/Preferences/com.apple.mobileipod.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.springboard.plist*")
+		(literal "${HOME}/Library/Caches/DateFormats.plist")
+	)
+)
+
+(deny file-write-setugid)
+
 (allow file-write-unlink
 	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-		(subpath "${FRONT_USER_HOME}")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-			(extension "com.apple.librarian.ubiquity-container")
-		)
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
 	)
 )
 (allow file-write-unlink
 	(require-all
-		(subpath "/private/var")
-		(subpath "${HOME}")
-		(require-any
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/DiagnosticLogs/Camera-latest.log")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/SpringBoard/.*(Lock|Home).+")
-		)
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 	)
 )
 (allow file-write-unlink
 	(require-all
-		(subpath "/private/var")
-		(subpath "${HOME}")
-		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(subpath "${HOME}/Library/AddressBook/Delegates")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(vnode-type REGULAR-FILE)
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(subpath "${HOME}/Library/AddressBook")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(subpath "${HOME}/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(extension "com.apple.classkit.read-write")
 		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit")
 			(require-all
-				(vnode-type DIRECTORY)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/ClassKit(/|$)")
 				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-					(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
 				)
 			)
-			(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
 		)
 	)
 )
 (allow file-write-unlink
-	(require-any
-		(subpath "/private/var/mnt")
-		(literal "${HOME}/Library/SpringBoard")
-		(subpath "${HOME}/Library/Caches/Snapshots/com.apple.camera")
-		(require-any
-			(subpath "${HOME}/Library/Siri")
-			(literal "${HOME}/Library/Logs/MobileSlideShow.log")
-			(literal "${HOME}/Library/Logs/awd/awd-Camera.log")
-			(literal "${HOME}/Library/Logs/awd/awd-MobileSlideShow.log")
-			(literal "${HOME}/Library/Logs/awd/awdComponent0x19.log")
-			(subpath "${HOME}/Library/Application Support/MobileSlideShow")
-			(subpath "${HOME}/Library/Application Support/iLifePageLayout")
-			(subpath "${HOME}/Library/Caches/com.apple.legacycamera")
-			(subpath "${HOME}/Library/Caches/com.apple.springboard.sharedimagecache/Wallpaper")
-		)
-		(subpath "${HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CloudPhotoLibrary.aslgroup")
-		(subpath "${HOME}/Library/SMS")
-		(subpath "${HOME}/Library/Logs/CrashReporter/DiagnosticLogs/Photos")
-		(subpath "${HOME}/Library/Cookies")
-		(literal "${HOME}/Library/Caches/com.apple.pep.configuration.plist")
-		(subpath "${HOME}/Library/Caches/com.apple.photos.peopleImageCache")
-		(subpath "${HOME}/Media/Debug")
-		(require-any
-			(subpath "${HOME}/Media/Safari")
-			(subpath "${HOME}/Documents/com.apple.camera.settings")
-			(subpath "${HOME}/Documents/com.apple.mobileslideshow.settings")
-			(subpath "${HOME}/Library/WebKit")
-			(literal "${HOME}/Library/Caches/Snapshots/com.apple.camera-*")
-			(literal "${HOME}/Library/Caches/Snapshots/com.apple.mobileslideshow-*")
-			(subpath "${HOME}/Library/Caches/Snapshots/com.apple.mobileslideshow")
-			(subpath "${HOME}/Library/Saved Application State/com.apple.camera\\.savedState")
-			(subpath "${HOME}/Library/Saved Application State/com.apple.mobileslideshow\\.savedState")
-		)
-		(subpath "${HOME}/Media/MediaAnalysis")
-		(subpath "/private/var/tmp")
-		(subpath "${HOME}/Media/PhotoData")
-		(subpath "${HOME}/Media/Memories")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.camera")
-			(subpath "${HOME}/Library/Caches/com.apple.mobileslideshow")
-		)
-		(literal "${HOME}/Library/Preferences/com.apple.dataaccess.launchd")
+	(require-all
+		(extension "com.apple.fileprovider.read-write")
 		(require-any
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.camera")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileslideshow")
-		)
-		(subpath "${HOME}/Media/DCIM")
-		(subpath "${HOME}/Media/Photos")
-		(subpath "${PROCESS_TEMP_DIR}")
-		(subpath "${HOME}/Library/WebClips")
+			(require-any
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+			)
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
 	)
 )
-(deny file-write-unlink
+(allow file-write-unlink
 	(require-all
 		(extension "com.apple.sandbox.application-group")
 		(require-any

 		)
 	)
 )
-(deny file-write-unlink
+(allow file-write-unlink
 	(require-all
 		(extension "com.apple.sandbox.container")
 		(require-any

 		)
 	)
 )
-(deny file-write-unlink
+(allow file-write-unlink
 	(require-all
-		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-only"))
-		(require-not (extension "com.apple.app-sandbox.read"))
-		(require-not (extension "com.apple.app-sandbox.read-write"))
-		(require-not (extension "com.apple.sandbox.executable"))
-		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-write"))
+		(vnode-type DIRECTORY REGULAR-FILE)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.photos.peopleImageCache")
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(vnode-type DIRECTORY REGULAR-FILE SYMLINK)
 		(require-any
-			(subpath "${ANY_USER_HOME}/Containers")
-			(subpath "/private/var/containers")
+			(subpath "/private/var/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+		)
+		(extension "com.apple.revisiond.staging")
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(vnode-type DIRECTORY REGULAR-FILE)
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.camera")
+			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.mobileslideshow")
 		)
 	)
 )
-(deny file-write-unlink
+(allow file-write-unlink
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(subpath "${HOME}/Library/Caches/com.apple.keyboards")
+	)
+)
+(allow file-write-unlink
 	(require-all
 		(signing-identifier "com.apple.camera.lockscreen")
 		(extension "com.apple.sandbox.container")

 		)
 	)
 )
-(deny file-write-unlink
-	(require-any
-		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-		(literal "${ANY_USER_HOME}/Library/Preferences/com.apple.mobileipod.plist")
-		(literal "${HOME}/Library/Preferences/com.apple.springboard.plist*")
-		(literal "${HOME}/Library/Caches/DateFormats.plist")
-	)
-)
-
-(allow file-write-xattr
+(allow file-write-unlink
 	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(subpath "${HOME}/Library/AddressBook/Delegates")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+		(subpath "${FRONT_USER_HOME}")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+			(extension "com.apple.librarian.ubiquity-container")
+		)
 	)
 )
-(allow file-write-xattr
+(allow file-write-unlink
 	(require-all
 		(subpath "/private/var")
 		(subpath "${HOME}")

 		)
 	)
 )
-(allow file-write-xattr
-	(require-all
-		(subpath "${HOME}/Library/Mobile Documents")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-)
-(allow file-write-xattr
+(allow file-write-unlink
 	(require-all
-		(extension "com.apple.classkit.read-write")
+		(subpath "/private/var")
+		(subpath "${HOME}")
+		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit")
 			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/ClassKit(/|$)")
+				(vnode-type DIRECTORY)
 				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+					(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
 				)
 			)
+			(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
 		)
 	)
 )
-(allow file-write-xattr
-	(require-all
-		(extension "com.apple.fileprovider.read-write")
+(allow file-write-unlink
+	(require-any
+		(subpath "/private/var/mnt")
+		(literal "${HOME}/Library/SpringBoard")
+		(subpath "${HOME}/Library/Caches/Snapshots/com.apple.camera")
 		(require-any
-			(require-any
-				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd")
-				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
-				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
-			)
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
-				(subpath "${FRONT_USER_HOME}")
-			)
+			(subpath "${HOME}/Library/Siri")
+			(literal "${HOME}/Library/Logs/MobileSlideShow.log")
+			(literal "${HOME}/Library/Logs/awd/awd-Camera.log")
+			(literal "${HOME}/Library/Logs/awd/awd-MobileSlideShow.log")
+			(literal "${HOME}/Library/Logs/awd/awdComponent0x19.log")
+			(subpath "${HOME}/Library/Application Support/MobileSlideShow")
+			(subpath "${HOME}/Library/Application Support/iLifePageLayout")
+			(subpath "${HOME}/Library/Caches/com.apple.legacycamera")
+			(subpath "${HOME}/Library/Caches/com.apple.springboard.sharedimagecache/Wallpaper")
 		)
+		(subpath "${HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CloudPhotoLibrary.aslgroup")
+		(subpath "${HOME}/Library/SMS")
+		(subpath "${HOME}/Library/Logs/CrashReporter/DiagnosticLogs/Photos")
+		(subpath "${HOME}/Library/Cookies")
+		(literal "${HOME}/Library/Caches/com.apple.pep.configuration.plist")
+		(subpath "${HOME}/Library/Caches/com.apple.photos.peopleImageCache")
+		(subpath "${HOME}/Media/Debug")
+		(require-any
+			(subpath "${HOME}/Media/Safari")
+			(subpath "${HOME}/Documents/com.apple.camera.settings")
+			(subpath "${HOME}/Documents/com.apple.mobileslideshow.settings")
+			(subpath "${HOME}/Library/WebKit")
+			(literal "${HOME}/Library/Caches/Snapshots/com.apple.camera-*")
+			(literal "${HOME}/Library/Caches/Snapshots/com.apple.mobileslideshow-*")
+			(subpath "${HOME}/Library/Caches/Snapshots/com.apple.mobileslideshow")
+			(subpath "${HOME}/Library/Saved Application State/com.apple.camera\\.savedState")
+			(subpath "${HOME}/Library/Saved Application State/com.apple.mobileslideshow\\.savedState")
+		)
+		(subpath "${HOME}/Media/MediaAnalysis")
+		(subpath "/private/var/tmp")
+		(subpath "${HOME}/Media/PhotoData")
+		(subpath "${HOME}/Media/Memories")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.camera")
+			(subpath "${HOME}/Library/Caches/com.apple.mobileslideshow")
+		)
+		(literal "${HOME}/Library/Preferences/com.apple.dataaccess.launchd")
+		(require-any
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.camera")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileslideshow")
+		)
+		(subpath "${HOME}/Media/DCIM")
+		(subpath "${HOME}/Media/Photos")
+		(subpath "${PROCESS_TEMP_DIR}")
+		(subpath "${HOME}/Library/WebClips")
 	)
 )
-(allow file-write-xattr
-	(require-all
-		(process-attribute is-apple-signed-executable)
-		(subpath "${HOME}/Library/Caches/com.apple.keyboards")
-	)
-)
-(allow file-write-xattr
+(deny file-write-unlink
 	(require-all
-		(subpath "/private/var")
-		(subpath "${HOME}")
-		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+		(extension "com.apple.sandbox.application-group")
 		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
 			(require-all
-				(vnode-type DIRECTORY)
+				(subpath "/private/var")
 				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-					(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 				)
 			)
-			(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
 		)
 	)
 )
-(allow file-write-xattr
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-)
-(allow file-write-xattr
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-)
-(allow file-write-xattr
-	(require-all
-		(vnode-type REGULAR-FILE)
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(subpath "${HOME}/Library/AddressBook")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
-	)
-)
-(allow file-write-xattr
+(deny file-write-unlink
 	(require-all
-		(signing-identifier "com.apple.camera.lockscreen")
 		(extension "com.apple.sandbox.container")
 		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/SyncedPreferences")
 			(require-all
 				(subpath "/private/var")
 				(require-any
 					(require-all
 						(subpath "/private/var/PersonaVolumes")
 						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$")
+								(signing-identifier "com.apple.camera.lockscreen")
+							)
 							(require-all
 								(require-any
 									(subpath "${FRONT_USER_HOME}")
 									(subpath "${HOME}")
 								)
 								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
+									(require-all
+										(regex #"((((((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)")
+										(signing-identifier "com.apple.camera.lockscreen")
+									)
 									(require-all
 										(signing-identifier "com.apple.camera.lockscreen")
-										(subpath "/private/var")
-										(extension "com.apple.sandbox.container")
 										(require-any
 											(require-all
 												(subpath "/private/var/PersonaVolumes")
 												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
 													(require-all
 														(require-any
 															(subpath "${FRONT_USER_HOME}")
 															(subpath "${HOME}")
 														)
-														(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+														(require-any
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+															(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+														)
 													)
 												)
 											)

 													(subpath "${FRONT_USER_HOME}")
 													(subpath "${HOME}")
 												)
-												(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+												(require-any
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+													(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+												)
 											)
+											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
 										)
 									)
 								)

 							(subpath "${HOME}")
 						)
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
+							(require-all
+								(regex #"((((((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)")
+								(signing-identifier "com.apple.camera.lockscreen")
+							)
 							(require-all
 								(signing-identifier "com.apple.camera.lockscreen")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
 								(require-any
 									(require-all
 										(subpath "/private/var/PersonaVolumes")
 										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
 											(require-all
 												(require-any
 													(subpath "${FRONT_USER_HOME}")
 													(subpath "${HOME}")
 												)
-												(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+												(require-any
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+													(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+												)
 											)
 										)
 									)

 											(subpath "${FRONT_USER_HOME}")
 											(subpath "${HOME}")
 										)
-										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+										)
 									)
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
 								)
 							)
 						)
 					)
 					(require-all
 						(signing-identifier "com.apple.camera.lockscreen")
-						(subpath "/private/var")
-						(extension "com.apple.sandbox.container")
 						(require-any
 							(require-all
 								(subpath "/private/var/PersonaVolumes")
 								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
 									(require-all
 										(require-any
 											(subpath "${FRONT_USER_HOME}")
 											(subpath "${HOME}")
 										)
-										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+										)
 									)
 								)
 							)

 									(subpath "${FRONT_USER_HOME}")
 									(subpath "${HOME}")
 								)
-								(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+								)
 							)
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
 						)
 					)
 				)
 			)
-		)
-	)
-)
-(allow file-write-xattr
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-		(subpath "${FRONT_USER_HOME}")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-			(extension "com.apple.librarian.ubiquity-container")
-		)
-	)
-)
-(allow file-write-xattr
-	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.camera")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.mobileslideshow")
-		)
-	)
-)
-(allow file-write-xattr
-	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE SYMLINK)
-		(require-any
-			(subpath "/private/var/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-		)
-		(extension "com.apple.revisiond.staging")
-	)
-)
-(allow file-write-xattr
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						)
-					)
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-				)
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
-			)
-		)
-	)
-)
-(allow file-write-xattr
-	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
-		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.photos.peopleImageCache")
-	)
-)
-(allow file-write-xattr
-	(require-any
-		(literal "${HOME}/Library/SpringBoard")
-		(subpath "${HOME}/Library/Caches/Snapshots/com.apple.camera")
-		(require-any
-			(subpath "${HOME}/Library/Siri")
-			(literal "${HOME}/Library/Logs/MobileSlideShow.log")
-			(literal "${HOME}/Library/Logs/awd/awd-Camera.log")
-			(literal "${HOME}/Library/Logs/awd/awd-MobileSlideShow.log")
-			(literal "${HOME}/Library/Logs/awd/awdComponent0x19.log")
-			(subpath "${HOME}/Library/Application Support/MobileSlideShow")
-			(subpath "${HOME}/Library/Application Support/iLifePageLayout")
-			(subpath "${HOME}/Library/Caches/com.apple.legacycamera")
-			(subpath "${HOME}/Library/Caches/com.apple.springboard.sharedimagecache/Wallpaper")
-		)
-		(subpath "${HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CloudPhotoLibrary.aslgroup")
-		(subpath "${HOME}/Library/SMS")
-		(subpath "${HOME}/Library/Logs/CrashReporter/DiagnosticLogs/Photos")
-		(subpath "${HOME}/Library/Cookies")
-		(literal "${HOME}/Library/Caches/com.apple.pep.configuration.plist")
-		(subpath "${HOME}/Library/Caches/com.apple.photos.peopleImageCache")
-		(subpath "${HOME}/Media/Debug")
-		(require-any
-			(subpath "${HOME}/Media/Safari")
-			(subpath "${HOME}/Documents/com.apple.camera.settings")
-			(subpath "${HOME}/Documents/com.apple.mobileslideshow.settings")
-			(subpath "${HOME}/Library/WebKit")
-			(literal "${HOME}/Library/Caches/Snapshots/com.apple.camera-*")
-			(literal "${HOME}/Library/Caches/Snapshots/com.apple.mobileslideshow-*")
-			(subpath "${HOME}/Library/Caches/Snapshots/com.apple.mobileslideshow")
-			(subpath "${HOME}/Library/Saved Application State/com.apple.camera\\.savedState")
-			(subpath "${HOME}/Library/Saved Application State/com.apple.mobileslideshow\\.savedState")
-		)
-		(subpath "${HOME}/Media/MediaAnalysis")
-		(subpath "/private/var/tmp")
-		(subpath "${HOME}/Media/PhotoData")
-		(subpath "${HOME}/Media/Memories")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.camera")
-			(subpath "${HOME}/Library/Caches/com.apple.mobileslideshow")
-		)
-		(literal "${HOME}/Library/Preferences/com.apple.dataaccess.launchd")
-		(require-any
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.camera")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileslideshow")
-		)
-		(subpath "${HOME}/Media/DCIM")
-		(subpath "${HOME}/Media/Photos")
-		(subpath "${PROCESS_TEMP_DIR}")
-		(subpath "${HOME}/Library/WebClips")
-	)
-)
-(deny file-write-xattr
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
 			(require-all
-				(subpath "/private/var")
+				(signing-identifier "com.apple.camera.lockscreen")
 				(require-any
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
 					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(subpath "/private/var")
 						(require-any
 							(subpath "${FRONT_USER_HOME}")
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+							(subpath "${HOME}")
 						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
 					)
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 				)
 			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
-			)
 		)
 	)
 )
-(deny file-write-xattr
+(deny file-write-unlink
 	(require-all
 		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-only"))
 		(require-not (extension "com.apple.app-sandbox.read"))

 		)
 	)
 )
-(deny file-write-xattr
+(deny file-write-unlink
 	(require-all
 		(signing-identifier "com.apple.camera.lockscreen")
 		(extension "com.apple.sandbox.container")

 		)
 	)
 )
-(deny file-write-xattr
+(deny file-write-unlink
 	(require-any
 		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 		(literal "${ANY_USER_HOME}/Library/Preferences/com.apple.mobileipod.plist")

 			(global-name "com.apple.ScreenTimeAgent")
 			(global-name "com.apple.symptomsd")
 			(global-name "com.apple.businessservicesd")
+			(global-name "com.apple.AppSSO.service-xpc")
+			(require-any
+				(global-name "com.apple.coremedia.mediaparserd.mutablemovie.xpc")
+				(global-name "com.apple.coremedia.mediaplaybackd.mutablemovie.xpc")
+				(global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc")
+			)
+			(global-name "com.apple.symptoms.symptomsd.managed_events")
+			(global-name "com.apple.synapse.backlink-service")
+			(global-name "com.apple.coreduetd.people")
+			(require-any
+				(global-name "com.apple.coremedia.remotequeue")
+				(global-name "com.apple.coremedia.mediaplaybackd.audiodeviceclock.xpc")
+			)
+			(global-name "com.apple.coremedia.bytestream.xpc")
+			(global-name "com.apple.spotlight.IndexAgent")
+			(global-name "com.apple.coremedia.systemcontroller.xpc")
+			(global-name "com.apple.AccessibilityUIServer")
+			(require-any
+				(global-name "com.apple.iap2d.ExternalAccessory.distributednotification.server")
+				(global-name "com.apple.iaptransportd.ExternalAccessory.distributednotification.server")
+			)
+			(global-name "com.apple.accessibility.heard")
+			(require-any
+				(global-name "com.apple.timesync.manager")
+				(global-name "com.apple.timesync.expositor")
+			)
+			(global-name "com.apple.coremedia.admin")
+			(global-name "com.apple.ind.xpc")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.Music.MPMusicPlayerControllerInternal")
+			(global-name "com.apple.webprivacyd")
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.pegasus")
+			(global-name "com.apple.symptom_diagnostics")
+			(global-name "com.apple.coremedia.cameraviewfinder")
+			(global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc")
+			(global-name "com.apple.identityservicesd.embedded.auth")
+			(global-name "com.apple.privacyaccountingd")
+			(global-name "com.apple.corespotlightservice")
+			(global-name "com.apple.coremedia.mediaplaybackd.visualcontext.xpc")
+			(global-name "com.apple.medialibraryd.xpc")
+			(global-name "com.apple.coreduetd.knowledge")
+			(global-name "com.apple.ctkd.slot-client")
+			(global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc")
+			(require-any
+				(global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc")
+				(global-name "com.apple.coremedia.mediaparserd.formatreader.xpc")
+			)
+			(global-name "com.apple.coresymbolicationd")
+			(global-name "com.apple.cache_delete.public")
+			(global-name "com.apple.coremedia.mediaplaybackd.asset.xpc")
+			(global-name "com.apple.networkd")
+			(global-name "com.apple.coremedia.sandboxserver")
+			(global-name "com.apple.duetactivityscheduler")
+			(global-name "com.apple.mediastream.sharing")
 			(require-any
 				(global-name "com.apple.alarmkitservices")
 				(global-name "com.apple.arkit.service.location")

 				(global-name "com.apple.appprotectiond.extensioninfo")
 				(global-name "com.apple.appprotectiond.extensionmonitor")
 				(global-name "com.apple.VoiceOverTouch.drag.xpc")
+				(global-name "com.apple.TelephonyTransferService")
 				(global-name "com.apple.PassKitWrapperXPCServiceUI")
 				(global-name "com.apple.testmanagerd")
 				(global-name "com.apple.translation.text")

 				(global-name "com.apple.wirelessinsightsd.xpc")
 				(global-name "com.apple.DragUI.druid.source")
 				(global-name "com.apple.DragUI.druid.destination")
-				(global-name "com.apple.ThreadNetwork.xpc")
-				(global-name "com.apple.TelephonyTransferService")
 				(global-name "com.apple.relatived.status")
 				(global-name "com.apple.relatived.public")
 				(global-name "com.apple.relatived.tempest")

 				(global-name "com.apple.usernotifications.accessorynotifications")
 				(global-name "com.apple.uikit.eyedropperd.service")
 				(global-name "com.apple.uiintelligencesupport.agent")
-				(global-name "com.apple.AccessorySetupUI")
-				(global-name "com.apple.AppMigrationKitHelper")
-				(global-name "com.apple.AppTrackingTransparency.EnforcementService")
-				(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent")
-				(global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.CredentialUpdate")
-			)
-			(global-name "com.apple.AppSSO.service-xpc")
-			(require-any
-				(global-name "com.apple.coremedia.mediaparserd.mutablemovie.xpc")
-				(global-name "com.apple.coremedia.mediaplaybackd.mutablemovie.xpc")
-				(global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc")
-			)
-			(global-name "com.apple.symptoms.symptomsd.managed_events")
-			(global-name "com.apple.synapse.backlink-service")
-			(global-name "com.apple.coreduetd.people")
-			(require-any
-				(global-name "com.apple.coremedia.remotequeue")
-				(global-name "com.apple.coremedia.mediaplaybackd.audiodeviceclock.xpc")
-			)
-			(global-name "com.apple.coremedia.bytestream.xpc")
-			(global-name "com.apple.spotlight.IndexAgent")
-			(global-name "com.apple.coremedia.systemcontroller.xpc")
-			(global-name "com.apple.AccessibilityUIServer")
-			(require-any
-				(global-name "com.apple.iap2d.ExternalAccessory.distributednotification.server")
-				(global-name "com.apple.iaptransportd.ExternalAccessory.distributednotification.server")
-			)
-			(global-name "com.apple.accessibility.heard")
-			(require-any
-				(global-name "com.apple.timesync.manager")
-				(global-name "com.apple.timesync.expositor")
-			)
-			(global-name "com.apple.coremedia.admin")
-			(global-name "com.apple.ind.xpc")
-			(global-name "com.apple.iokit.powerdxpc")
-			(global-name "com.apple.Music.MPMusicPlayerControllerInternal")
-			(global-name "com.apple.webprivacyd")
-			(global-name "com.apple.PowerManagement.control")
-			(global-name "com.apple.pegasus")
-			(global-name "com.apple.symptom_diagnostics")
-			(global-name "com.apple.coremedia.cameraviewfinder")
-			(global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc")
-			(global-name "com.apple.identityservicesd.embedded.auth")
-			(global-name "com.apple.privacyaccountingd")
-			(global-name "com.apple.corespotlightservice")
-			(global-name "com.apple.coremedia.mediaplaybackd.visualcontext.xpc")
-			(global-name "com.apple.medialibraryd.xpc")
-			(global-name "com.apple.coreduetd.knowledge")
-			(global-name "com.apple.ctkd.slot-client")
-			(global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc")
-			(require-any
-				(global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc")
-				(global-name "com.apple.coremedia.mediaparserd.formatreader.xpc")
+				(global-name "com.apple.AccessorySetupUI")
+				(global-name "com.apple.AppMigrationKitHelper")
+				(global-name "com.apple.AppTrackingTransparency.EnforcementService")
+				(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent")
+				(global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.CredentialUpdate")
 			)
-			(global-name "com.apple.coresymbolicationd")
-			(global-name "com.apple.cache_delete.public")
-			(global-name "com.apple.coremedia.mediaplaybackd.asset.xpc")
-			(global-name "com.apple.networkd")
-			(global-name "com.apple.coremedia.sandboxserver")
-			(global-name "com.apple.duetactivityscheduler")
-			(global-name "com.apple.mediastream.sharing")
 			(global-name "com.apple.corerecents.recentsd")
 			(global-name "com.apple.coremedia.routingsessionmanager.xpc")
 			(global-name "com.apple.cfnetwork.AuthBrokerAgent")

 					(xpc-service-name "com.apple.ImageIOXPCService")
 				)
 			)
+			(require-all
+				(global-name "com.apple.ThreadNetwork.xpc")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
+					(xpc-service-name "com.apple.ImageIOXPCService")
+				)
+			)
 			(require-all
 				(global-name "com.apple.coreidvd.digital-presentment.xpc")
 				(require-any

 			(global-name "com.apple.ScreenTimeAgent")
 			(global-name "com.apple.symptomsd")
 			(global-name "com.apple.businessservicesd")
+			(global-name "com.apple.AppSSO.service-xpc")
+			(require-any
+				(global-name "com.apple.coremedia.mediaparserd.mutablemovie.xpc")
+				(global-name "com.apple.coremedia.mediaplaybackd.mutablemovie.xpc")
+				(global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc")
+			)
+			(global-name "com.apple.symptoms.symptomsd.managed_events")
+			(global-name "com.apple.synapse.backlink-service")
+			(global-name "com.apple.coreduetd.people")
+			(require-any
+				(global-name "com.apple.coremedia.remotequeue")
+				(global-name "com.apple.coremedia.mediaplaybackd.audiodeviceclock.xpc")
+			)
+			(global-name "com.apple.coremedia.bytestream.xpc")
+			(global-name "com.apple.spotlight.IndexAgent")
+			(global-name "com.apple.coremedia.systemcontroller.xpc")
+			(global-name "com.apple.AccessibilityUIServer")
+			(require-any
+				(global-name "com.apple.iap2d.ExternalAccessory.distributednotification.server")
+				(global-name "com.apple.iaptransportd.ExternalAccessory.distributednotification.server")
+			)
+			(global-name "com.apple.accessibility.heard")
+			(require-any
+				(global-name "com.apple.timesync.manager")
+				(global-name "com.apple.timesync.expositor")
+			)
+			(global-name "com.apple.coremedia.admin")
+			(global-name "com.apple.ind.xpc")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.Music.MPMusicPlayerControllerInternal")
+			(global-name "com.apple.webprivacyd")
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.pegasus")
+			(global-name "com.apple.symptom_diagnostics")
+			(global-name "com.apple.coremedia.cameraviewfinder")
+			(global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc")
+			(global-name "com.apple.identityservicesd.embedded.auth")
+			(global-name "com.apple.privacyaccountingd")
+			(global-name "com.apple.corespotlightservice")
+			(global-name "com.apple.coremedia.mediaplaybackd.visualcontext.xpc")
+			(global-name "com.apple.medialibraryd.xpc")
+			(global-name "com.apple.coreduetd.knowledge")
+			(global-name "com.apple.ctkd.slot-client")
+			(global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc")
+			(require-any
+				(global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc")
+				(global-name "com.apple.coremedia.mediaparserd.formatreader.xpc")
+			)
+			(global-name "com.apple.coresymbolicationd")
+			(global-name "com.apple.cache_delete.public")
+			(global-name "com.apple.coremedia.mediaplaybackd.asset.xpc")
+			(global-name "com.apple.networkd")
+			(global-name "com.apple.coremedia.sandboxserver")
+			(global-name "com.apple.duetactivityscheduler")
+			(global-name "com.apple.mediastream.sharing")
 			(require-any
 				(global-name "com.apple.alarmkitservices")
 				(global-name "com.apple.arkit.service.location")

 				(global-name "com.apple.appprotectiond.extensioninfo")
 				(global-name "com.apple.appprotectiond.extensionmonitor")
 				(global-name "com.apple.VoiceOverTouch.drag.xpc")
+				(global-name "com.apple.TelephonyTransferService")
 				(global-name "com.apple.PassKitWrapperXPCServiceUI")
 				(global-name "com.apple.testmanagerd")
 				(global-name "com.apple.translation.text")

 				(global-name "com.apple.wirelessinsightsd.xpc")
 				(global-name "com.apple.DragUI.druid.source")
 				(global-name "com.apple.DragUI.druid.destination")
-				(global-name "com.apple.ThreadNetwork.xpc")
-				(global-name "com.apple.TelephonyTransferService")
 				(global-name "com.apple.relatived.status")
 				(global-name "com.apple.relatived.public")
 				(global-name "com.apple.relatived.tempest")

 				(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent")
 				(global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.CredentialUpdate")
 			)
-			(global-name "com.apple.AppSSO.service-xpc")
-			(require-any
-				(global-name "com.apple.coremedia.mediaparserd.mutablemovie.xpc")
-				(global-name "com.apple.coremedia.mediaplaybackd.mutablemovie.xpc")
-				(global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc")
-			)
-			(global-name "com.apple.symptoms.symptomsd.managed_events")
-			(global-name "com.apple.synapse.backlink-service")
-			(global-name "com.apple.coreduetd.people")
-			(require-any
-				(global-name "com.apple.coremedia.remotequeue")
-				(global-name "com.apple.coremedia.mediaplaybackd.audiodeviceclock.xpc")
-			)
-			(global-name "com.apple.coremedia.bytestream.xpc")
-			(global-name "com.apple.spotlight.IndexAgent")
-			(global-name "com.apple.coremedia.systemcontroller.xpc")
-			(global-name "com.apple.AccessibilityUIServer")
-			(require-any
-				(global-name "com.apple.iap2d.ExternalAccessory.distributednotification.server")
-				(global-name "com.apple.iaptransportd.ExternalAccessory.distributednotification.server")
-			)
-			(global-name "com.apple.accessibility.heard")
-			(require-any
-				(global-name "com.apple.timesync.manager")
-				(global-name "com.apple.timesync.expositor")
-			)
-			(global-name "com.apple.coremedia.admin")
-			(global-name "com.apple.ind.xpc")
-			(global-name "com.apple.iokit.powerdxpc")
-			(global-name "com.apple.Music.MPMusicPlayerControllerInternal")
-			(global-name "com.apple.webprivacyd")
-			(global-name "com.apple.PowerManagement.control")
-			(global-name "com.apple.pegasus")
-			(global-name "com.apple.symptom_diagnostics")
-			(global-name "com.apple.coremedia.cameraviewfinder")
-			(global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc")
-			(global-name "com.apple.identityservicesd.embedded.auth")
-			(global-name "com.apple.privacyaccountingd")
-			(global-name "com.apple.corespotlightservice")
-			(global-name "com.apple.coremedia.mediaplaybackd.visualcontext.xpc")
-			(global-name "com.apple.medialibraryd.xpc")
-			(global-name "com.apple.coreduetd.knowledge")
-			(global-name "com.apple.ctkd.slot-client")
-			(global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc")
-			(require-any
-				(global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc")
-				(global-name "com.apple.coremedia.mediaparserd.formatreader.xpc")
-			)
-			(global-name "com.apple.coresymbolicationd")
-			(global-name "com.apple.cache_delete.public")
-			(global-name "com.apple.coremedia.mediaplaybackd.asset.xpc")
-			(global-name "com.apple.networkd")
-			(global-name "com.apple.coremedia.sandboxserver")
-			(global-name "com.apple.duetactivityscheduler")
-			(global-name "com.apple.mediastream.sharing")
 			(global-name "com.apple.corerecents.recentsd")
 			(global-name "com.apple.coremedia.routingsessionmanager.xpc")
 			(global-name "com.apple.cfnetwork.AuthBrokerAgent")

 					(xpc-service-name "com.apple.ImageIOXPCService")
 				)
 			)
+			(require-all
+				(global-name "com.apple.ThreadNetwork.xpc")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
+					(xpc-service-name "com.apple.ImageIOXPCService")
+				)
+			)
 			(require-all
 				(global-name "com.apple.coreidvd.digital-presentment.xpc")
 				(require-any

 			(global-name "com.apple.ScreenTimeAgent")
 			(global-name "com.apple.symptomsd")
 			(global-name "com.apple.businessservicesd")
+			(global-name "com.apple.AppSSO.service-xpc")
+			(require-any
+				(global-name "com.apple.coremedia.mediaparserd.mutablemovie.xpc")
+				(global-name "com.apple.coremedia.mediaplaybackd.mutablemovie.xpc")
+				(global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc")
+			)
+			(global-name "com.apple.symptoms.symptomsd.managed_events")
+			(global-name "com.apple.synapse.backlink-service")
+			(global-name "com.apple.coreduetd.people")
+			(require-any
+				(global-name "com.apple.coremedia.remotequeue")
+				(global-name "com.apple.coremedia.mediaplaybackd.audiodeviceclock.xpc")
+			)
+			(global-name "com.apple.coremedia.bytestream.xpc")
+			(global-name "com.apple.spotlight.IndexAgent")
+			(global-name "com.apple.coremedia.systemcontroller.xpc")
+			(global-name "com.apple.AccessibilityUIServer")
+			(require-any
+				(global-name "com.apple.iap2d.ExternalAccessory.distributednotification.server")
+				(global-name "com.apple.iaptransportd.ExternalAccessory.distributednotification.server")
+			)
+			(global-name "com.apple.accessibility.heard")
+			(require-any
+				(global-name "com.apple.timesync.manager")
+				(global-name "com.apple.timesync.expositor")
+			)
+			(global-name "com.apple.coremedia.admin")
+			(global-name "com.apple.ind.xpc")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.Music.MPMusicPlayerControllerInternal")
+			(global-name "com.apple.webprivacyd")
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.pegasus")
+			(global-name "com.apple.symptom_diagnostics")
+			(global-name "com.apple.coremedia.cameraviewfinder")
+			(global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc")
+			(global-name "com.apple.identityservicesd.embedded.auth")
+			(global-name "com.apple.privacyaccountingd")
+			(global-name "com.apple.corespotlightservice")
+			(global-name "com.apple.coremedia.mediaplaybackd.visualcontext.xpc")
+			(global-name "com.apple.medialibraryd.xpc")
+			(global-name "com.apple.coreduetd.knowledge")
+			(global-name "com.apple.ctkd.slot-client")
+			(global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc")
+			(require-any
+				(global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc")
+				(global-name "com.apple.coremedia.mediaparserd.formatreader.xpc")
+			)
+			(global-name "com.apple.coresymbolicationd")
+			(global-name "com.apple.cache_delete.public")
+			(global-name "com.apple.coremedia.mediaplaybackd.asset.xpc")
+			(global-name "com.apple.networkd")
+			(global-name "com.apple.coremedia.sandboxserver")
+			(global-name "com.apple.duetactivityscheduler")
+			(global-name "com.apple.mediastream.sharing")
 			(require-any
 				(global-name "com.apple.alarmkitservices")
 				(global-name "com.apple.arkit.service.location")

 				(global-name "com.apple.appprotectiond.extensioninfo")
 				(global-name "com.apple.appprotectiond.extensionmonitor")
 				(global-name "com.apple.VoiceOverTouch.drag.xpc")
+				(global-name "com.apple.TelephonyTransferService")
 				(global-name "com.apple.PassKitWrapperXPCServiceUI")
 				(global-name "com.apple.testmanagerd")
 				(global-name "com.apple.translation.text")

 				(global-name "com.apple.wirelessinsightsd.xpc")
 				(global-name "com.apple.DragUI.druid.source")
 				(global-name "com.apple.DragUI.druid.destination")
-				(global-name "com.apple.ThreadNetwork.xpc")
-				(global-name "com.apple.TelephonyTransferService")
 				(global-name "com.apple.relatived.status")
 				(global-name "com.apple.relatived.public")
 				(global-name "com.apple.relatived.tempest")

 				(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent")
 				(global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.CredentialUpdate")
 			)
-			(global-name "com.apple.AppSSO.service-xpc")
-			(require-any
-				(global-name "com.apple.coremedia.mediaparserd.mutablemovie.xpc")
-				(global-name "com.apple.coremedia.mediaplaybackd.mutablemovie.xpc")
-				(global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc")
-			)
-			(global-name "com.apple.symptoms.symptomsd.managed_events")
-			(global-name "com.apple.synapse.backlink-service")
-			(global-name "com.apple.coreduetd.people")
-			(require-any
-				(global-name "com.apple.coremedia.remotequeue")
-				(global-name "com.apple.coremedia.mediaplaybackd.audiodeviceclock.xpc")
-			)
-			(global-name "com.apple.coremedia.bytestream.xpc")
-			(global-name "com.apple.spotlight.IndexAgent")
-			(global-name "com.apple.coremedia.systemcontroller.xpc")
-			(global-name "com.apple.AccessibilityUIServer")
-			(require-any
-				(global-name "com.apple.iap2d.ExternalAccessory.distributednotification.server")
-				(global-name "com.apple.iaptransportd.ExternalAccessory.distributednotification.server")
-			)
-			(global-name "com.apple.accessibility.heard")
-			(require-any
-				(global-name "com.apple.timesync.manager")
-				(global-name "com.apple.timesync.expositor")
-			)
-			(global-name "com.apple.coremedia.admin")
-			(global-name "com.apple.ind.xpc")
-			(global-name "com.apple.iokit.powerdxpc")
-			(global-name "com.apple.Music.MPMusicPlayerControllerInternal")
-			(global-name "com.apple.webprivacyd")
-			(global-name "com.apple.PowerManagement.control")
-			(global-name "com.apple.pegasus")
-			(global-name "com.apple.symptom_diagnostics")
-			(global-name "com.apple.coremedia.cameraviewfinder")
-			(global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc")
-			(global-name "com.apple.identityservicesd.embedded.auth")
-			(global-name "com.apple.privacyaccountingd")
-			(global-name "com.apple.corespotlightservice")
-			(global-name "com.apple.coremedia.mediaplaybackd.visualcontext.xpc")
-			(global-name "com.apple.medialibraryd.xpc")
-			(global-name "com.apple.coreduetd.knowledge")
-			(global-name "com.apple.ctkd.slot-client")
-			(global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc")
-			(require-any
-				(global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc")
-				(global-name "com.apple.coremedia.mediaparserd.formatreader.xpc")
-			)
-			(global-name "com.apple.coresymbolicationd")
-			(global-name "com.apple.cache_delete.public")
-			(global-name "com.apple.coremedia.mediaplaybackd.asset.xpc")
-			(global-name "com.apple.networkd")
-			(global-name "com.apple.coremedia.sandboxserver")
-			(global-name "com.apple.duetactivityscheduler")
-			(global-name "com.apple.mediastream.sharing")
 			(global-name "com.apple.corerecents.recentsd")
 			(global-name "com.apple.coremedia.routingsessionmanager.xpc")
 			(global-name "com.apple.cfnetwork.AuthBrokerAgent")

 					(xpc-service-name "com.apple.ImageIOXPCService")
 				)
 			)
+			(require-all
+				(global-name "com.apple.ThreadNetwork.xpc")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
+					(xpc-service-name "com.apple.ImageIOXPCService")
+				)
+			)
 			(require-all
 				(global-name "com.apple.coreidvd.digital-presentment.xpc")
 				(require-any
```

##### app-extension-enhanced-security

```diff

 
 (allow mach-lookup
 	(require-any
-		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```

##### apple-cloud-enhanced-security

```diff

 (allow mach-lookup
 	(require-any
 		(global-name "com.apple.logd.events")
-		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.cloudos.cb_bridged")
 		(global-name "com.apple.logd")
 		(extension "com.apple.security.exception.mach-lookup.global-name")

 		(global-name "com.apple.mobileassetd.v2")
 		(global-name "com.apple.coremedia.mediaparserd.utilities")
 		(global-name "com.apple.system.logger")
+		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.mobilegestalt.xpc")
 	)
 )
```

##### arquicklook

```diff

 (allow file-test-existence)
 (deny file-test-existence
 	(require-any
-		(require-any
-			(subpath "/bin")
-			(subpath "/sbin")
-			(subpath "/private/etc")
-			(subpath "/usr/bin")
-			(literal "/usr/share/terminfo")
-		)
 		(require-any
 			(subpath "/private/var/Managed Preferences/mobile")
 			(subpath "${HOME}/Library/SMS")

 			(subpath "${HOME}/Library/Application Support/CloudDocs/session/unprotected/containers")
 		)
 		(subpath "${HOME}/Library/Mobile Documents")
+		(require-any
+			(subpath "/bin")
+			(subpath "/sbin")
+			(subpath "/private/etc")
+			(subpath "/usr/bin")
+			(literal "/usr/share/terminfo")
+		)
 	)
 )
 
```

##### baseline

```diff

 )
 (allow iokit-open-service
 	(require-any
+		(profile-flag "autobox-client-telemetry")
 		(profile-flag "autobox-client")
 		(profile-flag "autobox-client-no-exception-entitlements")
-		(profile-flag "autobox-client-telemetry")
 	)
 )
 (deny iokit-open-service)
```

##### blastdoor-airlock

```diff

 
 (allow mach-lookup
 	(require-any
-		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```

##### blastdoor-ids

```diff

 	)
 )
 
-(allow mach-derive-port
-	(global-name "com.apple.analyticsd")
-)
-
 (allow mach-lookup
 	(require-any
-		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```

##### blastdoor-messages

```diff

 
 (allow mach-lookup
 	(require-any
-		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```

##### blastdoor-thumbnails

```diff

 
 (allow mach-lookup
 	(require-any
-		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```

##### classification-ui

```diff

 )
 (deny file-read*
 	(require-any
-		(subpath "/private/var/MobileAsset/Assets/com_apple_MobileAsset_LinguisticData")
 		(require-any
 			(subpath "/private/var/hardware/FactoryData")
 			(literal "/usr/standalone/firmware/apticket.der")

 			(subpath "/System/Library/Caches/com.apple.kernelcaches")
 			(literal "/System/Library/Caches/apticket.der")
 		)
+		(subpath "/private/var/MobileAsset/Assets/com_apple_MobileAsset_LinguisticData")
 	)
 )
 

 (allow file-test-existence)
 (deny file-test-existence
 	(require-any
+		(require-any
+			(subpath "/bin")
+			(subpath "/sbin")
+			(subpath "/private/etc")
+			(subpath "/usr/bin")
+			(literal "/usr/share/terminfo")
+		)
 		(require-any
 			(subpath "/private/var/Managed Preferences/mobile")
 			(subpath "${HOME}/Library/SMS")

 			(subpath "${HOME}/Library/Application Support/CloudDocs/session/unprotected/containers")
 		)
 		(subpath "${HOME}/Library/Mobile Documents")
-		(require-any
-			(subpath "/bin")
-			(subpath "/sbin")
-			(subpath "/private/etc")
-			(subpath "/usr/bin")
-			(literal "/usr/share/terminfo")
-		)
 	)
 )
 
```

##### com.apple.assistant.assistantd

```diff

 )
 (deny file-write-create
 	(require-any
-		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 		(literal "${HOME}/Library/Logs/CrashReporter/CFNetwork_*")
+		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 	)
 )
 
```

##### container

```diff

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.assessmentagent")
-		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
+		(global-name "com.apple.ThreadNetwork.xpc")
+		(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ak.anisette.xpc")
-		(require-any
-			(process-attribute is-apple-signed-executable)
-			(%entitlement-is-bool-true "com.apple.authkit.client")
-			(%entitlement-is-bool-true "com.apple.authkit.client.private")
-			(%entitlement-is-bool-true "com.apple.authkit.client.internal")
-		)
+		(global-name "com.apple.powerlog.plxpclogger.xpc")
+		(signing-identifier "com.apple.shortcuts")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.browserkitd")
-		(%entitlement-is-present "com.apple.developer.web-browser")
+		(global-name "com.apple.PowerManagement.control")
+		(signing-identifier "com.apple.shortcuts")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.identityservicesd.embedded.auth")
+		(global-name "com.apple.VideoSubscriberAccount.videosubscriptionsd")
 		(require-any
-			(signing-identifier "com.apple.shortcuts")
-			(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
-			(require-any
-				(signing-identifier "com.apple.shortcuts.watch")
-				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
-			)
+			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.internal")
+			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.web-sources.read-write")
+			(%entitlement-is-bool-true "com.apple.smoot.subscriptionservice")
+			(%entitlement-is-bool-true "com.apple.developer.video-subscription-registration")
+			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.all-sources.read-only")
 		)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(process-attribute is-apple-signed-executable)
-		(require-any
-			(global-name "com.apple.SharedWebCredentials")
-			(global-name "com.apple.dataaccess.dataaccessd")
-			(global-name "com.apple.exchangesyncd")
-			(xpc-service-name "com.apple.ctcategories.service")
-			(xpc-service-name "com.apple.LORemoteUIPinService")
-		)
+		(global-name "com.apple.coreidvd.digital-presentment.xpc")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.iokit.powerdxpc")
-		(signing-identifier "com.apple.shortcuts")
+		(global-name "com.apple.browserkitd")
+		(%entitlement-is-present "com.apple.developer.web-browser")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.enterprise.licensing")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.developer.arkit.barcode-detection.allow")
-			(%entitlement-is-bool-true "com.apple.developer.arkit.object-tracking-parameter-adjustment.allow")
-			(%entitlement-is-bool-true "com.apple.developer.arkit.shared-coordinate-space.allow")
-			(%entitlement-is-bool-true "com.apple.developer.screen-capture.include-passthrough")
-			(%entitlement-is-bool-true "com.apple.developer.avfoundation.uvc-device-access")
-			(%entitlement-is-bool-true "com.apple.developer.coreml.neural-engine-access")
-			(%entitlement-is-bool-true "com.apple.developer.arkit.main-camera-access.allow")
-			(%entitlement-is-bool-true "com.apple.developer.protected-content")
-			(%entitlement-is-bool-true "com.apple.developer.window-body-follow")
-			(%entitlement-is-bool-true "com.apple.developer.arkit.camera-region.allow")
-			(%entitlement-is-present "com.apple.developer.app-compute-category")
-		)
+		(global-name "com.apple.seserviced.credential.manager")
+		(%entitlement-is-present "com.apple.developer.secure-element-credential")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
-		(require-any
-			(global-name "com.apple.securityd")
-			(global-name "com.apple.trustd")
-			(global-name "com.apple.commcenter.xpc")
-			(global-name "com.apple.commcenter.cupolicy.xpc")
-			(global-name "com.apple.usymptomsd")
-			(global-name "com.apple.symptomsd")
-			(global-name "com.apple.symptoms.symptomsd.managed_events")
-			(global-name "com.apple.SystemConfiguration.DNSConfiguration")
-			(global-name "com.apple.SystemConfiguration.NetworkInformation")
-			(global-name "com.apple.SystemConfiguration.helper")
-			(global-name "com.apple.SystemConfiguration.configd")
-			(global-name "com.apple.SystemConfiguration.PPPController")
-			(global-name "com.apple.SystemConfiguration.SCNetworkReachability")
-		)
+		(global-name "com.apple.FileCoordination")
+		(signing-identifier "com.apple.Music")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.PowerManagement.control")
-		(signing-identifier "com.apple.shortcuts")
+		(global-name "com.apple.uikit.viewservice.*")
+		(require-any
+			(global-name "com.apple.cloudkit.partlycloudd")
+			(require-any
+				(global-name "com.apple.cloudd.debug")
+				(global-name "com.apple.cloudkit.partlycloudd.debug")
+			)
+			(global-name #"^com[.]apple[.]uikit[.]viewservice[.].+")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(xpc-service-name "com.apple.StreamingUnzipService")
-		(require-any
-			(signing-identifier "com.apple.Home")
-			(signing-identifier "com.apple.Home.HomeControlService")
-		)
+		(global-name "com.apple.lsd.xpc")
+		(signing-identifier "com.apple.mobilesafari")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(signing-identifier "com.apple.Maps")
+		(process-attribute is-apple-signed-executable)
 		(require-any
-			(global-name "com.apple.powerlog.plxpclogger.xpc")
-			(global-name "com.apple.iokit.powerdxpc")
-			(global-name "com.apple.PowerManagement.control")
-			(global-name "com.apple.nanomaps.xpc.Navigation")
-			(global-name "com.apple.nanomaps.xpc.GeoServices.Navigation")
-			(global-name "com.apple.assistant.analytics")
+			(global-name "com.apple.SharedWebCredentials")
+			(global-name "com.apple.dataaccess.dataaccessd")
+			(global-name "com.apple.exchangesyncd")
+			(xpc-service-name "com.apple.ctcategories.service")
+			(xpc-service-name "com.apple.LORemoteUIPinService")
 		)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.mobilestoredemod")
-		(%entitlement-is-present "com.apple.private.mobilestoredemo.enabledemo")
+		(global-name "com.apple.nanoprefsync")
+		(signing-identifier "com.apple.Music")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.FileCoordination")
-		(signing-identifier "com.apple.Music")
+		(xpc-service-name "com.apple.StreamingUnzipService")
+		(require-any
+			(signing-identifier "com.apple.Home")
+			(signing-identifier "com.apple.Home.HomeControlService")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.messages.critical-messaging")
-		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+		(signing-identifier "com.apple.mobilemail")
+		(require-any
+			(global-name "com.apple.nanoprefsync")
+			(global-name "com.apple.routined.registration")
+			(global-name "com.apple.backupd")
+			(global-name "com.apple.sharingd.nsxpc")
+			(global-name "com.apple.bulletindistributord.server")
+			(global-name "com.apple.identityservicesd.embedded.auth")
+			(global-name "com.apple.mobilemail")
+			(global-name "com.apple.harvestd.manager")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.uikit.viewservice.*")
-		(require-any
-			(global-name "com.apple.cloudkit.partlycloudd")
-			(require-any
-				(global-name "com.apple.cloudd.debug")
-				(global-name "com.apple.cloudkit.partlycloudd.debug")
-			)
-			(global-name #"^com[.]apple[.]uikit[.]viewservice[.].+")
-		)
+		(local-name "com.apple.iphone.axserver")
+		(%entitlement-is-bool-true "com.apple.accessibility.api")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.coreidvd.digital-presentment.xpc")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
+		(global-name "com.apple.cache_delete")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.mobile.deleted.AllowFreeSpace")
+			(%entitlement-is-present "com.apple.private.CacheDelete")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.cache_delete")
+		(signing-identifier "com.apple.Maps")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.mobile.deleted.AllowFreeSpace")
-			(%entitlement-is-present "com.apple.private.CacheDelete")
+			(global-name "com.apple.powerlog.plxpclogger.xpc")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.nanomaps.xpc.Navigation")
+			(global-name "com.apple.nanomaps.xpc.GeoServices.Navigation")
+			(global-name "com.apple.assistant.analytics")
 		)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(signing-identifier "com.apple.mobilemail")
+		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
 		(require-any
-			(global-name "com.apple.nanoprefsync")
-			(global-name "com.apple.routined.registration")
-			(global-name "com.apple.backupd")
-			(global-name "com.apple.sharingd.nsxpc")
-			(global-name "com.apple.bulletindistributord.server")
-			(global-name "com.apple.identityservicesd.embedded.auth")
-			(global-name "com.apple.mobilemail")
-			(global-name "com.apple.harvestd.manager")
+			(global-name "com.apple.securityd")
+			(global-name "com.apple.trustd")
+			(global-name "com.apple.commcenter.xpc")
+			(global-name "com.apple.commcenter.cupolicy.xpc")
+			(global-name "com.apple.usymptomsd")
+			(global-name "com.apple.symptomsd")
+			(global-name "com.apple.symptoms.symptomsd.managed_events")
+			(global-name "com.apple.SystemConfiguration.DNSConfiguration")
+			(global-name "com.apple.SystemConfiguration.NetworkInformation")
+			(global-name "com.apple.SystemConfiguration.helper")
+			(global-name "com.apple.SystemConfiguration.configd")
+			(global-name "com.apple.SystemConfiguration.PPPController")
+			(global-name "com.apple.SystemConfiguration.SCNetworkReachability")
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.safarifetcherd")
-		(signing-identifier "com.apple.mobilesafari")
+		(global-name "com.apple.identityservicesd.embedded.auth")
+		(require-any
+			(signing-identifier "com.apple.shortcuts")
+			(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
+			(require-any
+				(signing-identifier "com.apple.shortcuts.watch")
+				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+			)
+		)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.lsd.xpc")
-		(signing-identifier "com.apple.mobilesafari")
+		(global-name "com.apple.enterprise.licensing")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.developer.arkit.barcode-detection.allow")
+			(%entitlement-is-bool-true "com.apple.developer.arkit.object-tracking-parameter-adjustment.allow")
+			(%entitlement-is-bool-true "com.apple.developer.arkit.shared-coordinate-space.allow")
+			(%entitlement-is-bool-true "com.apple.developer.screen-capture.include-passthrough")
+			(%entitlement-is-bool-true "com.apple.developer.avfoundation.uvc-device-access")
+			(%entitlement-is-bool-true "com.apple.developer.coreml.neural-engine-access")
+			(%entitlement-is-bool-true "com.apple.developer.arkit.main-camera-access.allow")
+			(%entitlement-is-bool-true "com.apple.developer.protected-content")
+			(%entitlement-is-bool-true "com.apple.developer.window-body-follow")
+			(%entitlement-is-bool-true "com.apple.developer.arkit.camera-region.allow")
+			(%entitlement-is-present "com.apple.developer.app-compute-category")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(local-name "com.apple.iphone.axserver")
-		(%entitlement-is-bool-true "com.apple.accessibility.api")
+		(global-name "com.apple.ak.anisette.xpc")
+		(require-any
+			(process-attribute is-apple-signed-executable)
+			(%entitlement-is-bool-true "com.apple.authkit.client")
+			(%entitlement-is-bool-true "com.apple.authkit.client.private")
+			(%entitlement-is-bool-true "com.apple.authkit.client.internal")
+		)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.VideoSubscriberAccount.videosubscriptionsd")
+		(global-name "com.apple.nanoprefsync")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.internal")
-			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.web-sources.read-write")
-			(%entitlement-is-bool-true "com.apple.smoot.subscriptionservice")
-			(%entitlement-is-bool-true "com.apple.developer.video-subscription-registration")
-			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.all-sources.read-only")
+			(signing-identifier "com.apple.Health")
+			(signing-identifier "com.apple.PassbookUIService")
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.nanoprefsync")
-		(require-any
-			(signing-identifier "com.apple.Health")
-			(signing-identifier "com.apple.PassbookUIService")
-		)
+		(global-name "com.apple.messages.critical-messaging")
+		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.nanoprefsync")
-		(signing-identifier "com.apple.Music")
+		(global-name "com.apple.merchantd.storage")
+		(require-any
+			(%entitlement-is-present "com.apple.developer.proximity-reader.payment.acceptance")
+			(require-all
+				(process-attribute is-apple-signed-executable)
+				(global-name "com.apple.dataaccess.dataaccessd")
+			)
+		)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.seserviced.credential.manager")
-		(%entitlement-is-present "com.apple.developer.secure-element-credential")
+		(global-name "com.apple.safarifetcherd")
+		(signing-identifier "com.apple.mobilesafari")
 	)
 )
 (allow mach-lookup

 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.assessmentagent")
+		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.personad.xpc")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.powerlog.plxpclogger.xpc")
+		(global-name "com.apple.iokit.powerdxpc")
 		(signing-identifier "com.apple.shortcuts")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.merchantd.storage")
-		(require-any
-			(%entitlement-is-present "com.apple.developer.proximity-reader.payment.acceptance")
-			(require-all
-				(process-attribute is-apple-signed-executable)
-				(global-name "com.apple.dataaccess.dataaccessd")
-			)
-		)
+		(global-name "com.apple.mobilestoredemod")
+		(%entitlement-is-present "com.apple.private.mobilestoredemo.enabledemo")
 	)
 )
 (allow mach-lookup

 		)
 		(global-name "com.apple.symptomsd")
 		(global-name "com.apple.businessservicesd")
+		(global-name "com.apple.AppSSO.service-xpc")
+		(require-any
+			(global-name "com.apple.coremedia.mediaparserd.mutablemovie.xpc")
+			(global-name "com.apple.coremedia.mediaplaybackd.mutablemovie.xpc")
+			(global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc")
+		)
+		(global-name "com.apple.webfilterd")
+		(global-name "com.apple.symptoms.symptomsd.managed_events")
+		(global-name "com.apple.synapse.backlink-service")
+		(require-any
+			(global-name "com.apple.coremedia.remotequeue")
+			(global-name "com.apple.coremedia.mediaplaybackd.audiodeviceclock.xpc")
+		)
+		(global-name "com.apple.coremedia.bytestream.xpc")
+		(global-name "com.apple.VoiceOverTouch.xpc")
+		(global-name "com.apple.coremedia.systemcontroller.xpc")
+		(global-name "com.apple.AccessibilityUIServer")
+		(require-any
+			(global-name "com.apple.timesync.manager")
+			(global-name "com.apple.timesync.expositor")
+		)
+		(global-name "com.apple.biome.access.user")
+		(global-name "com.apple.audio.AURemoteIOServer")
+		(global-name "com.apple.coremedia.admin")
+		(global-name "com.apple.gamecenter")
+		(global-name "com.apple.iokit.powerdxpc")
+		(global-name "PurpleSystemEventPort")
+		(global-name "com.apple.Music.MPMusicPlayerControllerInternal")
+		(global-name "com.apple.pairedsyncd.syncstate")
+		(global-name "com.apple.webprivacyd")
+		(global-name "com.apple.PowerManagement.control")
+		(global-name "com.apple.pegasus")
+		(global-name "com.apple.iapd")
+		(global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc")
+		(global-name "com.apple.Music.MPMusicPlayerMigServerExists")
+		(global-name "com.apple.privacyaccountingd")
+		(global-name "com.apple.corespotlightservice")
+		(global-name "com.apple.coremedia.mediaplaybackd.visualcontext.xpc")
+		(global-name "com.apple.medialibraryd.xpc")
+		(global-name "com.apple.ctkd.slot-client")
+		(global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc")
+		(require-any
+			(global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc")
+			(global-name "com.apple.coremedia.mediaparserd.formatreader.xpc")
+		)
+		(global-name "com.apple.webinspector")
+		(global-name "com.apple.coresymbolicationd")
+		(global-name "com.apple.cache_delete.public")
+		(global-name "com.apple.imagent.embedded.auth")
+		(global-name "com.apple.coremedia.mediaplaybackd.asset.xpc")
+		(global-name "com.apple.networkd")
+		(global-name "com.apple.coremedia.sandboxserver")
+		(global-name "com.apple.duetactivityscheduler")
+		(global-name "com.apple.quicklook.ThumbnailsAgent")
+		(global-name "com.apple.mediastream.sharing")
+		(global-name "com.apple.mobilecheckpoint.checkpointd")
 		(require-any
 			(global-name "com.apple.alarmkitservices")
 			(global-name "com.apple.arkit.service.location")

 			(global-name "com.apple.appprotectiond.extensioninfo")
 			(global-name "com.apple.appprotectiond.extensionmonitor")
 			(global-name "com.apple.VoiceOverTouch.drag.xpc")
+			(global-name "com.apple.TelephonyTransferService")
 			(global-name "com.apple.PassKitWrapperXPCServiceUI")
 			(global-name "com.apple.testmanagerd")
 			(global-name "com.apple.translation.text")

 			(global-name "com.apple.wirelessinsightsd.xpc")
 			(global-name "com.apple.DragUI.druid.source")
 			(global-name "com.apple.DragUI.druid.destination")
-			(global-name "com.apple.ThreadNetwork.xpc")
-			(global-name "com.apple.TelephonyTransferService")
 			(global-name "com.apple.relatived.status")
 			(global-name "com.apple.relatived.public")
 			(global-name "com.apple.relatived.tempest")

 			(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent")
 			(global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.CredentialUpdate")
 		)
-		(global-name "com.apple.AppSSO.service-xpc")
-		(require-any
-			(global-name "com.apple.coremedia.mediaparserd.mutablemovie.xpc")
-			(global-name "com.apple.coremedia.mediaplaybackd.mutablemovie.xpc")
-			(global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc")
-		)
-		(global-name "com.apple.webfilterd")
-		(global-name "com.apple.symptoms.symptomsd.managed_events")
-		(global-name "com.apple.synapse.backlink-service")
-		(require-any
-			(global-name "com.apple.coremedia.remotequeue")
-			(global-name "com.apple.coremedia.mediaplaybackd.audiodeviceclock.xpc")
-		)
-		(global-name "com.apple.coremedia.bytestream.xpc")
-		(global-name "com.apple.VoiceOverTouch.xpc")
-		(global-name "com.apple.coremedia.systemcontroller.xpc")
-		(global-name "com.apple.AccessibilityUIServer")
-		(require-any
-			(global-name "com.apple.timesync.manager")
-			(global-name "com.apple.timesync.expositor")
-		)
-		(global-name "com.apple.biome.access.user")
-		(global-name "com.apple.audio.AURemoteIOServer")
-		(global-name "com.apple.coremedia.admin")
-		(global-name "com.apple.gamecenter")
-		(global-name "com.apple.iokit.powerdxpc")
-		(global-name "PurpleSystemEventPort")
-		(global-name "com.apple.Music.MPMusicPlayerControllerInternal")
-		(global-name "com.apple.pairedsyncd.syncstate")
-		(global-name "com.apple.webprivacyd")
-		(global-name "com.apple.PowerManagement.control")
-		(global-name "com.apple.pegasus")
-		(global-name "com.apple.iapd")
-		(global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc")
-		(global-name "com.apple.Music.MPMusicPlayerMigServerExists")
-		(global-name "com.apple.privacyaccountingd")
-		(global-name "com.apple.corespotlightservice")
-		(global-name "com.apple.coremedia.mediaplaybackd.visualcontext.xpc")
-		(global-name "com.apple.medialibraryd.xpc")
-		(global-name "com.apple.ctkd.slot-client")
-		(global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc")
-		(require-any
-			(global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc")
-			(global-name "com.apple.coremedia.mediaparserd.formatreader.xpc")
-		)
-		(global-name "com.apple.webinspector")
-		(global-name "com.apple.coresymbolicationd")
-		(global-name "com.apple.cache_delete.public")
-		(global-name "com.apple.imagent.embedded.auth")
-		(global-name "com.apple.coremedia.mediaplaybackd.asset.xpc")
-		(global-name "com.apple.networkd")
-		(global-name "com.apple.coremedia.sandboxserver")
-		(global-name "com.apple.duetactivityscheduler")
-		(global-name "com.apple.quicklook.ThumbnailsAgent")
-		(global-name "com.apple.mediastream.sharing")
-		(global-name "com.apple.mobilecheckpoint.checkpointd")
 		(global-name "com.apple.corerecents.recentsd")
 		(global-name "com.apple.coremedia.routingsessionmanager.xpc")
 		(require-any

 		(xpc-service-name "com.apple.accessibility.heard")
 		(xpc-service-name "com.apple.MTLCompilerService")
 		(xpc-service-name "com.apple.accessibility.AccessibilityUIServer")
-		(xpc-service-name "com.apple.backgroundassets.managed.helper.service")
+		(require-any
+			(xpc-service-name "com.apple.WebKit.WebContent")
+			(xpc-service-name "com.apple.WebKit.Networking")
+		)
 		(extension "com.apple.security.exception.mach-lookup.local-name")
 		(require-any
 			(xpc-service-name "com.apple.WebKit.Model")

 			(xpc-service-name "com.apple.WebKit.WebContent.EnhancedSecurity")
 		)
 		(xpc-service-name "com.apple.coremedia.decompressionsession.xpc")
-		(require-any
-			(xpc-service-name "com.apple.WebKit.WebContent")
-			(xpc-service-name "com.apple.WebKit.Networking")
-		)
+		(xpc-service-name "com.apple.backgroundassets.managed.helper.service")
 		(xpc-service-name "com.apple.coremedia.compressionsession.xpc")
 		(global-name "com.apple.locationd.synchronous")
 		(global-name "com.apple.locationd.registration")
```

##### duetexpertd

```diff

 )
 (deny mach-lookup
 	(require-any
-		(xpc-service-name "com.apple.WebKit.*")
 		(xpc-service-name "com.apple.CoreGraphics.CGPDFService")
+		(xpc-service-name "com.apple.WebKit.*")
 	)
 )
 
```

##### gamed

```diff

 		)
 	)
 )
+(deny file-write-create
+	(literal "${HOME}/Library/Logs/CrashReporter/CFNetwork_*")
+)
 (deny file-write-create
 	(require-all
 		(subpath "/private/var")

 		)
 	)
 )
-(deny file-write-create
-	(literal "${HOME}/Library/Logs/CrashReporter/CFNetwork_*")
-)
 (deny file-write-create
 	(require-all
 		(extension "com.apple.sandbox.application-group")
```

##### location-push-service

```diff

 	)
 )
 (deny file-write-data
-	(require-any
-		(literal "${HOME}/Library/Caches/DateFormats.plist")
-		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-	)
-)
-
-(allow file-write-flags
-	(require-all
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-	)
-)
-(allow file-write-flags
-	(require-all
-		(extension "com.apple.librarian.ubiquity-container")
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-			(subpath "${HOME}/Library/Mobile Documents")
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-				(subpath "${FRONT_USER_HOME}")
-			)
-		)
-	)
-)
-(allow file-write-flags
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						)
-					)
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-				)
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
-			)
-		)
-	)
-)
-(allow file-write-flags
-	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE SYMLINK)
-		(require-any
-			(subpath "/private/var/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-		)
-		(extension "com.apple.revisiond.staging")
-	)
-)
-(allow file-write-flags
-	(require-all
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/SyncedPreferences")
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
-									(require-all
-										(extension "com.apple.sandbox.container")
-										(require-any
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-													(require-all
-														(require-any
-															(subpath "${FRONT_USER_HOME}")
-															(subpath "${HOME}")
-														)
-														(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-													)
-												)
-											)
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
-							(require-all
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-											)
-										)
-									)
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var")
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-									)
-								)
-							)
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(deny file-write-flags
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						)
-					)
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-				)
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
-			)
-		)
-	)
-)
-(deny file-write-flags
-	(require-all
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/SyncedPreferences")
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
-									(require-all
-										(extension "com.apple.sandbox.container")
-										(require-any
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-													(require-all
-														(require-any
-															(subpath "${FRONT_USER_HOME}")
-															(subpath "${HOME}")
-														)
-														(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-													)
-												)
-											)
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$")
-							(require-all
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-											)
-										)
-									)
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var")
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-									)
-								)
-							)
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(deny file-write-flags
 	(require-any
 		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 		(literal "${HOME}/Library/Caches/DateFormats.plist")

 )
 (deny file-write-unlink
 	(require-any
-		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 		(literal "${HOME}/Library/Caches/DateFormats.plist")
+		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 	)
 )
 
```

##### maild

```diff

 )
 (deny file-write*
 	(require-any
-		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 		(literal "${HOME}/Library/Preferences/com.apple.springboard.plist*")
 		(literal "${HOME}/Library/Caches/DateFormats.plist")
+		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 	)
 )
 

 	)
 )
 
+(allow file-write-finderinfo
+	(require-all
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+	)
+)
+(allow file-write-finderinfo
+	(require-all
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(require-any
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/AddressBook")
+					(require-all
+						(require-any
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+						)
+						(extension "com.apple.revisiond.staging")
+					)
+				)
+			)
+			(subpath "${HOME}/Library/AddressBook/Delegates")
+		)
+	)
+)
+(allow file-write-finderinfo
+	(require-all
+		(extension "com.apple.librarian.ubiquity-container")
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+			(subpath "${HOME}/Library/Mobile Documents")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(allow file-write-finderinfo
+	(require-all
+		(subpath "${HOME}/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-finderinfo
+	(require-all
+		(extension "com.apple.classkit.read-write")
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/ClassKit(/|$)")
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+			)
+		)
+	)
+)
+(allow file-write-finderinfo
+	(require-all
+		(extension "com.apple.fileprovider.read-write")
+		(require-any
+			(require-any
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+			)
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(allow file-write-finderinfo
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(allow file-write-finderinfo
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-finderinfo
+	(require-all
+		(vnode-type DIRECTORY REGULAR-FILE SYMLINK)
+		(require-any
+			(subpath "/private/var/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+		)
+		(extension "com.apple.revisiond.staging")
+	)
+)
+(allow file-write-finderinfo
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+		(subpath "${FRONT_USER_HOME}")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+			(extension "com.apple.librarian.ubiquity-container")
+		)
+	)
+)
+(allow file-write-finderinfo
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(subpath "${HOME}/Library/Caches/com.apple.keyboards")
+	)
+)
+(deny file-write-finderinfo
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(deny file-write-finderinfo
+	(require-any
+		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
+		(literal "${HOME}/Library/Preferences/com.apple.springboard.plist*")
+		(literal "${HOME}/Library/Caches/DateFormats.plist")
+	)
+)
+
 (allow file-write-flags
 	(require-all
 		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")

 		)
 	)
 )
-(allow file-write-flags
-	(require-all
-		(subpath "${HOME}/Library/Mobile Documents")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-)
-(allow file-write-flags
+(allow file-write-flags
+	(require-all
+		(subpath "${HOME}/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-flags
+	(require-all
+		(extension "com.apple.classkit.read-write")
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/ClassKit(/|$)")
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+			)
+		)
+	)
+)
+(allow file-write-flags
+	(require-all
+		(extension "com.apple.fileprovider.read-write")
+		(require-any
+			(require-any
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+			)
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(allow file-write-flags
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(allow file-write-flags
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-flags
+	(require-all
+		(vnode-type DIRECTORY REGULAR-FILE SYMLINK)
+		(require-any
+			(subpath "/private/var/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+		)
+		(extension "com.apple.revisiond.staging")
+	)
+)
+(allow file-write-flags
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+		(subpath "${FRONT_USER_HOME}")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+			(extension "com.apple.librarian.ubiquity-container")
+		)
+	)
+)
+(allow file-write-flags
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(subpath "${HOME}/Library/Caches/com.apple.keyboards")
+	)
+)
+(deny file-write-flags
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(deny file-write-flags
+	(require-any
+		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
+		(literal "${HOME}/Library/Preferences/com.apple.springboard.plist*")
+		(literal "${HOME}/Library/Caches/DateFormats.plist")
+	)
+)
+
+(allow file-write-mode
+	(require-all
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+	)
+)
+(allow file-write-mode
+	(require-all
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(require-any
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/AddressBook")
+					(require-all
+						(require-any
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+						)
+						(extension "com.apple.revisiond.staging")
+					)
+				)
+			)
+			(subpath "${HOME}/Library/AddressBook/Delegates")
+		)
+	)
+)
+(allow file-write-mode
+	(require-all
+		(extension "com.apple.librarian.ubiquity-container")
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+			(subpath "${HOME}/Library/Mobile Documents")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(allow file-write-mode
+	(require-all
+		(subpath "${HOME}/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-mode
+	(require-all
+		(extension "com.apple.classkit.read-write")
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/ClassKit(/|$)")
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+			)
+		)
+	)
+)
+(allow file-write-mode
+	(require-all
+		(extension "com.apple.fileprovider.read-write")
+		(require-any
+			(require-any
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+			)
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(allow file-write-mode
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(allow file-write-mode
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-mode
+	(require-all
+		(vnode-type DIRECTORY REGULAR-FILE SYMLINK)
+		(require-any
+			(subpath "/private/var/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+		)
+		(extension "com.apple.revisiond.staging")
+	)
+)
+(allow file-write-mode
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+		(subpath "${FRONT_USER_HOME}")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+			(extension "com.apple.librarian.ubiquity-container")
+		)
+	)
+)
+(allow file-write-mode
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(subpath "${HOME}/Library/Caches/com.apple.keyboards")
+	)
+)
+(deny file-write-mode
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(deny file-write-mode
+	(require-any
+		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
+		(literal "${HOME}/Library/Preferences/com.apple.springboard.plist*")
+		(literal "${HOME}/Library/Caches/DateFormats.plist")
+	)
+)
+
+(deny file-write-setugid)
+
+(allow file-write-times
+	(require-all
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+	)
+)
+(allow file-write-times
+	(require-all
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(require-any
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/AddressBook")
+					(require-all
+						(require-any
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+						)
+						(extension "com.apple.revisiond.staging")
+					)
+				)
+			)
+			(subpath "${HOME}/Library/AddressBook/Delegates")
+		)
+	)
+)
+(allow file-write-times
+	(require-all
+		(extension "com.apple.librarian.ubiquity-container")
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+			(subpath "${HOME}/Library/Mobile Documents")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(allow file-write-times
+	(require-all
+		(subpath "${HOME}/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-times
+	(require-all
+		(extension "com.apple.classkit.read-write")
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/ClassKit(/|$)")
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+			)
+		)
+	)
+)
+(allow file-write-times
+	(require-all
+		(extension "com.apple.fileprovider.read-write")
+		(require-any
+			(require-any
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+			)
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(allow file-write-times
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(allow file-write-times
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-times
+	(require-all
+		(vnode-type DIRECTORY REGULAR-FILE SYMLINK)
+		(require-any
+			(subpath "/private/var/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+		)
+		(extension "com.apple.revisiond.staging")
+	)
+)
+(allow file-write-times
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+		(subpath "${FRONT_USER_HOME}")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+			(extension "com.apple.librarian.ubiquity-container")
+		)
+	)
+)
+(allow file-write-times
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(subpath "${HOME}/Library/Caches/com.apple.keyboards")
+	)
+)
+(deny file-write-times
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(deny file-write-times
+	(require-any
+		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
+		(literal "${HOME}/Library/Preferences/com.apple.springboard.plist*")
+		(literal "${HOME}/Library/Caches/DateFormats.plist")
+	)
+)
+
+(allow file-write-unlink
+	(require-all
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(subpath "${FRONT_USER_HOME}/Library/IdentityServices")
+		(extension "com.apple.identityservices.deliver")
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(subpath "${HOME}/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(extension "com.apple.librarian.ubiquity-container")
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+			(subpath "${HOME}/Library/Mobile Documents")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(require-any
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/AddressBook")
+					(require-all
+						(require-any
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+						)
+						(extension "com.apple.revisiond.staging")
+					)
+				)
+			)
+			(subpath "${HOME}/Library/AddressBook/Delegates")
+		)
+	)
+)
+(allow file-write-unlink
 	(require-all
 		(extension "com.apple.classkit.read-write")
 		(require-any

 		)
 	)
 )
-(allow file-write-flags
+(allow file-write-unlink
 	(require-all
 		(extension "com.apple.fileprovider.read-write")
 		(require-any

 		)
 	)
 )
-(allow file-write-flags
+(allow file-write-unlink
 	(require-all
 		(extension "com.apple.sandbox.application-group")
 		(require-any

 		)
 	)
 )
-(allow file-write-flags
+(allow file-write-unlink
 	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
 	)
 )
-(allow file-write-flags
+(allow file-write-unlink
 	(require-all
 		(vnode-type DIRECTORY REGULAR-FILE SYMLINK)
 		(require-any

 		(extension "com.apple.revisiond.staging")
 	)
 )
-(allow file-write-flags
+(allow file-write-unlink
 	(require-all
 		(subpath "/private/var")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")

 		)
 	)
 )
-(allow file-write-flags
+(allow file-write-unlink
 	(require-all
 		(process-attribute is-apple-signed-executable)
 		(subpath "${HOME}/Library/Caches/com.apple.keyboards")
 	)
 )
-(deny file-write-flags
+(deny file-write-unlink
 	(require-all
 		(extension "com.apple.sandbox.application-group")
 		(require-any

 		)
 	)
 )
-(deny file-write-flags
+(deny file-write-unlink
 	(require-any
+		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 		(literal "${HOME}/Library/Preferences/com.apple.springboard.plist*")
 		(literal "${HOME}/Library/Caches/DateFormats.plist")
-		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 	)
 )
 
-(deny file-write-setugid)
-
-(allow file-write-unlink
+(allow file-write-xattr
 	(require-all
 		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
 	)
 )
-(allow file-write-unlink
-	(require-all
-		(subpath "${FRONT_USER_HOME}/Library/IdentityServices")
-		(extension "com.apple.identityservices.deliver")
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(subpath "${HOME}/Library/Mobile Documents")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(extension "com.apple.librarian.ubiquity-container")
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-			(subpath "${HOME}/Library/Mobile Documents")
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-				(subpath "${FRONT_USER_HOME}")
-			)
-		)
-	)
-)
-(allow file-write-unlink
+(allow file-write-xattr
 	(require-all
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")

 		)
 	)
 )
-(allow file-write-unlink
+(allow file-write-xattr
+	(require-all
+		(extension "com.apple.librarian.ubiquity-container")
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+			(subpath "${HOME}/Library/Mobile Documents")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+				(subpath "${FRONT_USER_HOME}")
+			)
+		)
+	)
+)
+(allow file-write-xattr
+	(require-all
+		(subpath "${HOME}/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-write-xattr
 	(require-all
 		(extension "com.apple.classkit.read-write")
 		(require-any

 		)
 	)
 )
-(allow file-write-unlink
+(allow file-write-xattr
 	(require-all
 		(extension "com.apple.fileprovider.read-write")
 		(require-any

 		)
 	)
 )
-(allow file-write-unlink
+(allow file-write-xattr
 	(require-all
 		(extension "com.apple.sandbox.application-group")
 		(require-any

 		)
 	)
 )
-(allow file-write-unlink
+(allow file-write-xattr
 	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 	)
 )
-(allow file-write-unlink
+(allow file-write-xattr
 	(require-all
 		(vnode-type DIRECTORY REGULAR-FILE SYMLINK)
 		(require-any

 		(extension "com.apple.revisiond.staging")
 	)
 )
-(allow file-write-unlink
+(allow file-write-xattr
 	(require-all
 		(subpath "/private/var")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")

 		)
 	)
 )
-(allow file-write-unlink
+(allow file-write-xattr
 	(require-all
 		(process-attribute is-apple-signed-executable)
 		(subpath "${HOME}/Library/Caches/com.apple.keyboards")
 	)
 )
-(deny file-write-unlink
+(deny file-write-xattr
 	(require-all
 		(extension "com.apple.sandbox.application-group")
 		(require-any

 		)
 	)
 )
-(deny file-write-unlink
+(deny file-write-xattr
 	(require-any
 		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 		(literal "${HOME}/Library/Preferences/com.apple.springboard.plist*")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.seserviced.credential.manager")
-		(%entitlement-is-present "com.apple.developer.secure-element-credential")
+		(global-name "com.apple.assessmentagent")
+		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
 	)
 )
 (allow mach-lookup

 		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.seserviced.credential.manager")
+		(%entitlement-is-present "com.apple.developer.secure-element-credential")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.ExposureNotification")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.assessmentagent")
-		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
+		(global-name "com.apple.ThreadNetwork.xpc")
+		(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
 	)
 )
 (allow mach-lookup

 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.MusicKit.UI")
+		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.ak.anisette.xpc")

 		)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
-		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.ak.auth.xpc")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.MusicKit.UI")
-		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+		(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
+		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
 	)
 )
 (allow mach-lookup

 		)
 		(global-name "com.apple.symptomsd")
 		(global-name "com.apple.businessservicesd")
+		(global-name "com.apple.AppSSO.service-xpc")
+		(global-name "com.apple.accountsd.oauthsigner")
+		(require-any
+			(global-name "com.apple.coremedia.mediaparserd.mutablemovie.xpc")
+			(global-name "com.apple.coremedia.mediaplaybackd.mutablemovie.xpc")
+			(global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc")
+		)
+		(global-name "com.apple.healthd.server")
+		(global-name "com.apple.webfilterd")
+		(global-name "com.apple.symptoms.symptomsd.managed_events")
+		(global-name "com.apple.synapse.backlink-service")
+		(require-any
+			(global-name "com.apple.coremedia.remotequeue")
+			(global-name "com.apple.coremedia.mediaplaybackd.audiodeviceclock.xpc")
+		)
+		(global-name "com.apple.coremedia.bytestream.xpc")
+		(global-name "com.apple.VoiceOverTouch.xpc")
+		(global-name "com.apple.spotlight.IndexAgent")
+		(global-name "com.apple.coremedia.systemcontroller.xpc")
+		(global-name "com.apple.AccessibilityUIServer")
+		(require-any
+			(global-name "com.apple.timesync.manager")
+			(global-name "com.apple.timesync.expositor")
+		)
+		(global-name "com.apple.audio.AURemoteIOServer")
+		(global-name "com.apple.coremedia.admin")
+		(global-name "com.apple.gamecenter")
+		(global-name "PurpleSystemEventPort")
+		(global-name "com.apple.bulletindistributord.server")
+		(global-name "com.apple.Music.MPMusicPlayerControllerInternal")
+		(global-name "com.apple.pairedsyncd.syncstate")
+		(global-name "com.apple.webprivacyd")
+		(global-name "com.apple.mobile.softwareupdated")
+		(global-name "com.apple.pegasus")
+		(global-name "com.apple.iapd")
+		(global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc")
+		(global-name "com.apple.Music.MPMusicPlayerMigServerExists")
+		(global-name "com.apple.privacyaccountingd")
+		(global-name "com.apple.corespotlightservice")
+		(global-name "com.apple.coremedia.mediaplaybackd.visualcontext.xpc")
+		(global-name "com.apple.medialibraryd.xpc")
+		(global-name "com.apple.ctkd.slot-client")
+		(global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc")
+		(require-any
+			(global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc")
+			(global-name "com.apple.coremedia.mediaparserd.formatreader.xpc")
+		)
+		(global-name "com.apple.webinspector")
+		(global-name "com.apple.coresymbolicationd")
+		(global-name "com.apple.cache_delete.public")
+		(global-name "com.apple.imagent.embedded.auth")
+		(global-name "com.apple.coremedia.mediaplaybackd.asset.xpc")
+		(global-name "com.apple.networkd")
+		(global-name "com.apple.coremedia.sandboxserver")
+		(global-name "com.apple.duetactivityscheduler")
+		(global-name "com.apple.quicklook.ThumbnailsAgent")
+		(global-name "com.apple.mediastream.sharing")
+		(global-name "com.apple.mobilecheckpoint.checkpointd")
 		(require-any
 			(global-name "com.apple.alarmkitservices")
 			(global-name "com.apple.arkit.service.location")

 			(global-name "com.apple.appprotectiond.extensioninfo")
 			(global-name "com.apple.appprotectiond.extensionmonitor")
 			(global-name "com.apple.VoiceOverTouch.drag.xpc")
+			(global-name "com.apple.TelephonyTransferService")
 			(global-name "com.apple.PassKitWrapperXPCServiceUI")
 			(global-name "com.apple.testmanagerd")
 			(global-name "com.apple.translation.text")

 			(global-name "com.apple.wirelessinsightsd.xpc")
 			(global-name "com.apple.DragUI.druid.source")
 			(global-name "com.apple.DragUI.druid.destination")
-			(global-name "com.apple.ThreadNetwork.xpc")
-			(global-name "com.apple.TelephonyTransferService")
 			(global-name "com.apple.relatived.status")
 			(global-name "com.apple.relatived.public")
 			(global-name "com.apple.relatived.tempest")

 			(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent")
 			(global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.CredentialUpdate")
 		)
-		(global-name "com.apple.AppSSO.service-xpc")
-		(global-name "com.apple.accountsd.oauthsigner")
-		(require-any
-			(global-name "com.apple.coremedia.mediaparserd.mutablemovie.xpc")
-			(global-name "com.apple.coremedia.mediaplaybackd.mutablemovie.xpc")
-			(global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc")
-		)
-		(global-name "com.apple.healthd.server")
-		(global-name "com.apple.webfilterd")
-		(global-name "com.apple.symptoms.symptomsd.managed_events")
-		(global-name "com.apple.synapse.backlink-service")
-		(require-any
-			(global-name "com.apple.coremedia.remotequeue")
-			(global-name "com.apple.coremedia.mediaplaybackd.audiodeviceclock.xpc")
-		)
-		(global-name "com.apple.coremedia.bytestream.xpc")
-		(global-name "com.apple.VoiceOverTouch.xpc")
-		(global-name "com.apple.spotlight.IndexAgent")
-		(global-name "com.apple.coremedia.systemcontroller.xpc")
-		(global-name "com.apple.AccessibilityUIServer")
-		(require-any
-			(global-name "com.apple.timesync.manager")
-			(global-name "com.apple.timesync.expositor")
-		)
-		(global-name "com.apple.audio.AURemoteIOServer")
-		(global-name "com.apple.coremedia.admin")
-		(global-name "com.apple.gamecenter")
-		(global-name "PurpleSystemEventPort")
-		(global-name "com.apple.bulletindistributord.server")
-		(global-name "com.apple.Music.MPMusicPlayerControllerInternal")
-		(global-name "com.apple.pairedsyncd.syncstate")
-		(global-name "com.apple.webprivacyd")
-		(global-name "com.apple.mobile.softwareupdated")
-		(global-name "com.apple.pegasus")
-		(global-name "com.apple.iapd")
-		(global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc")
-		(global-name "com.apple.Music.MPMusicPlayerMigServerExists")
-		(global-name "com.apple.privacyaccountingd")
-		(global-name "com.apple.corespotlightservice")
-		(global-name "com.apple.coremedia.mediaplaybackd.visualcontext.xpc")
-		(global-name "com.apple.medialibraryd.xpc")
-		(global-name "com.apple.ctkd.slot-client")
-		(global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc")
-		(require-any
-			(global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc")
-			(global-name "com.apple.coremedia.mediaparserd.formatreader.xpc")
-		)
-		(global-name "com.apple.webinspector")
-		(global-name "com.apple.coresymbolicationd")
-		(global-name "com.apple.cache_delete.public")
-		(global-name "com.apple.imagent.embedded.auth")
-		(global-name "com.apple.coremedia.mediaplaybackd.asset.xpc")
-		(global-name "com.apple.networkd")
-		(global-name "com.apple.coremedia.sandboxserver")
-		(global-name "com.apple.duetactivityscheduler")
-		(global-name "com.apple.quicklook.ThumbnailsAgent")
-		(global-name "com.apple.mediastream.sharing")
-		(global-name "com.apple.mobilecheckpoint.checkpointd")
 		(global-name "com.apple.corerecents.recentsd")
 		(global-name "com.apple.coremedia.routingsessionmanager.xpc")
 		(require-any
```

##### media-device-discovery-extension

```diff

 (allow file-test-existence)
 (deny file-test-existence
 	(require-any
+		(require-any
+			(subpath "/bin")
+			(subpath "/sbin")
+			(subpath "/private/etc")
+			(subpath "/usr/bin")
+			(literal "/usr/share/terminfo")
+		)
 		(require-any
 			(subpath "/private/var/Managed Preferences/mobile")
 			(subpath "${HOME}/Library/SMS")

 			(subpath "${HOME}/Library/Application Support/CloudDocs/session/unprotected/containers")
 		)
 		(subpath "${HOME}/Library/Mobile Documents")
-		(require-any
-			(subpath "/bin")
-			(subpath "/sbin")
-			(subpath "/private/etc")
-			(subpath "/usr/bin")
-			(literal "/usr/share/terminfo")
-		)
 	)
 )
 
```

##### message-filter

```diff

 (allow file-test-existence)
 (deny file-test-existence
 	(require-any
+		(require-any
+			(subpath "/bin")
+			(subpath "/sbin")
+			(subpath "/private/etc")
+			(subpath "/usr/bin")
+			(literal "/usr/share/terminfo")
+		)
 		(require-any
 			(subpath "/private/var/Managed Preferences/mobile")
 			(subpath "${HOME}/Library/SMS")

 			(subpath "${HOME}/Library/Application Support/CloudDocs/session/unprotected/containers")
 		)
 		(subpath "${HOME}/Library/Mobile Documents")
-		(require-any
-			(subpath "/bin")
-			(subpath "/sbin")
-			(subpath "/private/etc")
-			(subpath "/usr/bin")
-			(literal "/usr/share/terminfo")
-		)
 	)
 )
 
```

##### nearbyd

```diff

 )
 (deny file-write-create
 	(require-any
-		(literal "${HOME}/Library/Logs/CrashReporter/CFNetwork_*")
 		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
+		(literal "${HOME}/Library/Logs/CrashReporter/CFNetwork_*")
 	)
 )
 
```

##### network-filter

```diff

 (allow file-test-existence)
 (deny file-test-existence
 	(require-any
-		(require-any
-			(subpath "/bin")
-			(subpath "/sbin")
-			(subpath "/private/etc")
-			(subpath "/usr/bin")
-			(literal "/usr/share/terminfo")
-		)
 		(require-any
 			(subpath "/private/var/Managed Preferences/mobile")
 			(subpath "${HOME}/Library/SMS")

 			(subpath "${HOME}/Library/Application Support/CloudDocs/session/unprotected/containers")
 		)
 		(subpath "${HOME}/Library/Mobile Documents")
+		(require-any
+			(subpath "/bin")
+			(subpath "/sbin")
+			(subpath "/private/etc")
+			(subpath "/usr/bin")
+			(literal "/usr/share/terminfo")
+		)
 	)
 )
 
```

##### quicklook-thumbnail

```diff

 (allow file-test-existence)
 (deny file-test-existence
 	(require-any
-		(require-any
-			(subpath "/bin")
-			(subpath "/sbin")
-			(subpath "/private/etc")
-			(subpath "/usr/bin")
-			(literal "/usr/share/terminfo")
-		)
 		(require-any
 			(subpath "/private/var/Managed Preferences/mobile")
 			(subpath "${HOME}/Library/SMS")

 			(subpath "${HOME}/Library/Application Support/CloudDocs/session/unprotected/containers")
 		)
 		(subpath "${HOME}/Library/Mobile Documents")
+		(require-any
+			(subpath "/bin")
+			(subpath "/sbin")
+			(subpath "/private/etc")
+			(subpath "/usr/bin")
+			(literal "/usr/share/terminfo")
+		)
 	)
 )
 
```

##### quicklookd

```diff

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.messages.critical-messaging")
-		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+		(global-name "com.apple.assessmentagent")
+		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
-		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
+		(global-name "com.apple.seserviced.session")
+		(%entitlement-is-present "com.apple.developer.carkey.session")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.MomentsUIService")
-		(%entitlement-is-present "com.apple.developer.journal.allow")
+		(global-name "com.apple.messages.critical-messaging")
+		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ExposureNotification")
-		(%entitlement-is-present "com.apple.developer.exposure-notification")
+		(global-name "com.apple.coreidvd.digital-presentment.xpc")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.assessmentagent")
-		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
+		(global-name "com.apple.ThreadNetwork.xpc")
+		(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.SafetyKit")
+		(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.seserviced.session")
-		(%entitlement-is-present "com.apple.developer.carkey.session")
+		(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
+		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.SafetyKit")
-		(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
+		(global-name "com.apple.ExposureNotification")
+		(%entitlement-is-present "com.apple.developer.exposure-notification")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.coreidvd.digital-presentment.xpc")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
+		(global-name "com.apple.MomentsUIService")
+		(%entitlement-is-present "com.apple.developer.journal.allow")
 	)
 )
 (allow mach-lookup

 			(global-name "com.apple.coremedia.mediaplaybackd.figcontentkeysession.xpc")
 			(global-name "com.apple.coremedia.mediaplaybackd.figmetriceventtimeline.xpc")
 		)
+		(require-any
+			(global-name "com.apple.coremedia.mediaparserd.mutablemovie.xpc")
+			(global-name "com.apple.coremedia.mediaplaybackd.mutablemovie.xpc")
+			(global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc")
+		)
+		(require-any
+			(global-name "com.apple.timesync.manager")
+			(global-name "com.apple.timesync.expositor")
+		)
+		(global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc")
+		(global-name "com.apple.duetactivityscheduler")
 		(require-any
 			(global-name "com.apple.alarmkitservices")
 			(global-name "com.apple.arkit.service.location")

 			(global-name "com.apple.appprotectiond.extensioninfo")
 			(global-name "com.apple.appprotectiond.extensionmonitor")
 			(global-name "com.apple.VoiceOverTouch.drag.xpc")
+			(global-name "com.apple.TelephonyTransferService")
 			(global-name "com.apple.PassKitWrapperXPCServiceUI")
 			(global-name "com.apple.testmanagerd")
 			(global-name "com.apple.translation.text")

 			(global-name "com.apple.wirelessinsightsd.xpc")
 			(global-name "com.apple.DragUI.druid.source")
 			(global-name "com.apple.DragUI.druid.destination")
-			(global-name "com.apple.ThreadNetwork.xpc")
-			(global-name "com.apple.TelephonyTransferService")
 			(global-name "com.apple.relatived.status")
 			(global-name "com.apple.relatived.public")
 			(global-name "com.apple.relatived.tempest")

 			(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent")
 			(global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.CredentialUpdate")
 		)
-		(require-any
-			(global-name "com.apple.coremedia.mediaparserd.mutablemovie.xpc")
-			(global-name "com.apple.coremedia.mediaplaybackd.mutablemovie.xpc")
-			(global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc")
-		)
-		(require-any
-			(global-name "com.apple.timesync.manager")
-			(global-name "com.apple.timesync.expositor")
-		)
-		(global-name "com.apple.corespotlightservice")
-		(global-name "com.apple.duetactivityscheduler")
-		(global-name "com.apple.audioanalyticsd")
 		(require-any
 			(global-name "com.apple.airplay.endpoint.xpc")
 			(global-name "com.apple.mediaexperience.endpoint.xpc")

 		(global-name "com.apple.coremedia.mediaplaybackd.videocompositor.xpc")
 		(global-name "com.apple.Safari.SafeBrowsing.Service")
 		(xpc-service-name "com.apple.AGXCompilerService*")
+		(xpc-service-name "com.apple.imfoundation.IMRemoteURLConnectionAgent")
 		(xpc-service-name "com.apple.WebKit.WebAuthn")
 		(xpc-service-name "com.apple.MTLCompilerService")
 		(xpc-service-name "com.apple.accessibility.AccessibilityUIServer")

 		(global-name "com.apple.pegasus")
 		(global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc")
 		(global-name "com.apple.privacyaccountingd")
+		(global-name "com.apple.corespotlightservice")
 		(global-name "com.apple.coremedia.mediaplaybackd.visualcontext.xpc")
 		(global-name "com.apple.ctkd.slot-client")
-		(global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc")
 		(require-any
 			(global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc")
 			(global-name "com.apple.coremedia.mediaparserd.formatreader.xpc")

 			(global-name "com.apple.coremedia.capturesource")
 			(global-name "com.apple.coremedia.capturesession")
 		)
+		(global-name "com.apple.audioanalyticsd")
 		(global-name "com.apple.handwritingd.remoterecognition")
 		(global-name "com.apple.siri.VoiceShortcuts.xpc")
 		(require-any

 		(global-name "com.apple.triald.namespace-management")
 		(xpc-service-name "com.apple.siri.context.service")
 		(xpc-service-name "com.apple.intents.intents-helper")
-		(xpc-service-name "com.apple.imfoundation.IMRemoteURLConnectionAgent")
 		(xpc-service-name "com.apple.textkit.nsattributedstringagent")
 		(xpc-service-name "com.apple.accessibility.heard")
 		(global-name "com.apple.DeviceAccess.xpc")
```

##### restrictive-extension

```diff

 (allow file-test-existence)
 (deny file-test-existence
 	(require-any
-		(require-any
-			(subpath "/bin")
-			(subpath "/sbin")
-			(subpath "/private/etc")
-			(subpath "/usr/bin")
-			(literal "/usr/share/terminfo")
-		)
 		(require-any
 			(subpath "/private/var/Managed Preferences/mobile")
 			(subpath "${HOME}/Library/SMS")

 			(subpath "${HOME}/Library/Application Support/CloudDocs/session/unprotected/containers")
 		)
 		(subpath "${HOME}/Library/Mobile Documents")
+		(require-any
+			(subpath "/bin")
+			(subpath "/sbin")
+			(subpath "/private/etc")
+			(subpath "/usr/bin")
+			(literal "/usr/share/terminfo")
+		)
 	)
 )
 
```

##### searchpartyd

```diff

 )
 (deny file-write-create
 	(require-any
-		(literal "${HOME}/Library/Logs/CrashReporter/CFNetwork_*")
 		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
+		(literal "${HOME}/Library/Logs/CrashReporter/CFNetwork_*")
 	)
 )
 
```

##### watchlistd

```diff

 		(literal "${HOME}/Library/Caches/com.apple.persistentconnection.intervalcache.plist.lock")
 	)
 )
-(deny file-write-create
-	(literal "${HOME}/Library/Logs/CrashReporter/CFNetwork_*")
-)
 (deny file-write-create
 	(require-all
 		(subpath "/private/var")

 		)
 	)
 )
+(deny file-write-create
+	(literal "${HOME}/Library/Logs/CrashReporter/CFNetwork_*")
+)
 (deny file-write-create
 	(require-all
 		(extension "com.apple.sandbox.application-group")
```
