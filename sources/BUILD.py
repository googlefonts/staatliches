import os 
import subprocess

#os.chdir("sources")

# Info
try:
    print("**** Running Fontmake ******************************\n")
    subprocess.call(['fontmake', '-g', 'sources/staatliches-regular.glyphs', '-o', 'ttf',])
except:
    print("Error! Try installing Fontmake: https://github.com/googlei18n/fontmake")

# Info
print("\n**** Moving fonts to fonts directory *******************")
subprocess.call(['cp', 'master_ttf/Staatliches-Regular.ttf', 'fonts/',])
print("     [+] Done")

# Info
print("\n**** Removing build directories  ***********************")
subprocess.call(['rm', '-rf', 'master_ttf', 'master_ufo',])
print("     [+] Done")

os.chdir("fonts")
cwd = os.getcwd()
print("     In Directory:", cwd)
print("\n**** Run: ttfautohint  *********************************\n")
subprocess.call(['ttfautohint', '-I', 'Staatliches-Regular.ttf', 'Staatliches-Regular-Fix.ttf'])
subprocess.call(['cp', 'Staatliches-Regular-Fix.ttf', 'Staatliches-Regular.ttf'])
subprocess.call(['rm', '-rf', 'Staatliches-Regular-Fix.ttf'])
print("     [+] Done")

os.chdir("..")
subprocess.call(['tree'])
