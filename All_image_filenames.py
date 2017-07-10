<<<<<<< HEAD
import fnmatch
import os

images = [
		'*.jpeg',
		'*.jpg',
		'*.png'
	]
audio = [
 		'*.mp4'
 	]
matches = []
audio
for root, dirname, filenames in os.walk(r"D:\assignments&pdf\FlukeNetworks"):
	#print("=============",root)
	for extensions in images:
		#print("============>>>>>>>>>")
		for filename in fnmatch.filter(filenames, extensions):
			#print("******************************")
			matches.append(os.path.join(root, filename))

# for name in matches:
# 	if '.jpg' in name:
# 		print(name[name.rindex("\\") + 1 : len(name)])

matches = []
for root, dirname, audio_filename in os.walk(r'D:\\'):
	#print("=============",root)
	for audio_ext in audio:
		for audio_file in fnmatch.filter(audio_filename, audio_ext):
			matches.append(os.path.join(root, audio_file))

for audio_name in matches:
	if '.mp4' not in audio_name:
		print('NULL')
	else:
=======
import fnmatch
import os

images = [
		'*.jpeg',
		'*.jpg',
		'*.png'
	]
audio = [
 		'*.mp4'
 	]
matches = []
audio
for root, dirname, filenames in os.walk(r"D:\assignments&pdf\FlukeNetworks"):
	#print("=============",root)
	for extensions in images:
		#print("============>>>>>>>>>")
		for filename in fnmatch.filter(filenames, extensions):
			#print("******************************")
			matches.append(os.path.join(root, filename))

# for name in matches:
# 	if '.jpg' in name:
# 		print(name[name.rindex("\\") + 1 : len(name)])

matches = []
for root, dirname, audio_filename in os.walk(r'D:\\'):
	#print("=============",root)
	for audio_ext in audio:
		for audio_file in fnmatch.filter(audio_filename, audio_ext):
			matches.append(os.path.join(root, audio_file))

for audio_name in matches:
	if '.mp4' not in audio_name:
		print('NULL')
	else:
>>>>>>> e3c31845a6b27c35918232991ff964bb1069ba71
		print(audio_name[audio_name.rindex("\\") + 1:])